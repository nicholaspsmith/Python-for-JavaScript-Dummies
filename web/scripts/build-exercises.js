/**
 * Build script to generate exercise manifest and copy exercise files
 * Supports multiple runtimes: Python, React, and SQL
 * Run with: node scripts/build-exercises.js
 */

import { readdir, readFile, writeFile, mkdir, copyFile, rm, cp } from 'fs/promises';
import { existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = join(__dirname, '..', '..');
const OUTPUT_DIR = join(__dirname, '..', 'static', 'exercises');
const MANIFEST_PATH = join(__dirname, '..', 'src', 'lib', 'exercises-manifest.json');

// Exercise folder pattern: NN-category-name
const FOLDER_PATTERN = /^(\d{2})-(.+)$/;
// Python exercise file pattern: NN_exercise_name.py
const PYTHON_FILE_PATTERN = /^(\d{2})_(.+)\.py$/;
// SQL exercise file pattern: NN_exercise_name.sql
const SQL_FILE_PATTERN = /^(\d{2})_(.+)\.sql$/;
// React exercise folder pattern: NN_exercise_name (folder with exercise.json)
const REACT_FOLDER_PATTERN = /^(\d{2})_(.+)$/;

/**
 * Detect runtime type from folder name
 */
function detectRuntime(folderName) {
  if (folderName.includes('code-master')) return 'python';
  if (folderName.includes('react')) return 'react';
  if (folderName.includes('sql')) return 'sql';
  // Legacy support for old folder names
  if (folderName.match(/^\d{2}-(easy|medium|hard)$/)) return 'python';
  return 'python'; // Default
}

async function getExerciseFolders() {
  const entries = await readdir(ROOT_DIR, { withFileTypes: true });
  return entries
    .filter(entry => entry.isDirectory() && FOLDER_PATTERN.test(entry.name))
    .map(entry => entry.name)
    .sort();
}

async function getPythonExerciseFiles(folder) {
  const folderPath = join(ROOT_DIR, folder);
  const entries = await readdir(folderPath, { withFileTypes: true });
  return entries
    .filter(entry => entry.isFile() && PYTHON_FILE_PATTERN.test(entry.name))
    .map(entry => entry.name)
    .sort();
}

async function getSQLExerciseFiles(folder) {
  const folderPath = join(ROOT_DIR, folder);
  const entries = await readdir(folderPath, { withFileTypes: true });
  return entries
    .filter(entry => entry.isFile() && SQL_FILE_PATTERN.test(entry.name))
    .map(entry => entry.name)
    .sort();
}

async function getReactExerciseFolders(folder) {
  const folderPath = join(ROOT_DIR, folder);
  const entries = await readdir(folderPath, { withFileTypes: true });
  const exerciseFolders = [];

  for (const entry of entries) {
    if (entry.isDirectory() && REACT_FOLDER_PATTERN.test(entry.name)) {
      // Check if it has an exercise.json
      const exerciseJsonPath = join(folderPath, entry.name, 'exercise.json');
      if (existsSync(exerciseJsonPath)) {
        exerciseFolders.push(entry.name);
      }
    }
  }

  return exerciseFolders.sort();
}

function parseExerciseName(filename, pattern) {
  // Convert 01_variables_and_types.py -> Variables And Types
  const match = filename.match(pattern);
  if (!match) return filename;
  return match[2]
    .split('_')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function parseCategoryName(folder) {
  // Convert 01-code-master-easy -> Leetcode Easy
  const match = folder.match(FOLDER_PATTERN);
  if (!match) return folder;
  let name = match[2]
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');

  // Replace "Code Master" with "Leetcode"
  name = name.replace('Code Master', 'Leetcode');
  return name;
}

async function extractPythonDescription(filePath) {
  try {
    const content = await readFile(filePath, 'utf-8');
    // Extract first line of docstring as description
    const docstringMatch = content.match(/^"""[\s\S]*?"""/m);
    if (docstringMatch) {
      const lines = docstringMatch[0].split('\n');
      // Get first non-empty line after opening quotes
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i].replace(/^"""/, '').trim();
        if (line && !line.startsWith('=')) {
          return line;
        }
      }
    }
  } catch (e) {
    // Ignore errors
  }
  return '';
}

async function extractSQLDescription(filePath) {
  try {
    const content = await readFile(filePath, 'utf-8');
    // Extract title from first comment block
    const commentMatch = content.match(/^\/\*[\s\S]*?\*\//);
    if (commentMatch) {
      const lines = commentMatch[0].split('\n');
      // Get first non-empty line after opening comment
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i].replace(/^\/\*/, '').replace(/\*\/$/, '').trim();
        if (line && !line.startsWith('=') && !line.startsWith('-')) {
          return line;
        }
      }
    }
  } catch (e) {
    // Ignore errors
  }
  return '';
}

async function extractReactDescription(exerciseJsonPath) {
  try {
    const content = await readFile(exerciseJsonPath, 'utf-8');
    const config = JSON.parse(content);
    return config.title || '';
  } catch (e) {
    // Ignore errors
  }
  return '';
}

async function processPythonExercises(folder, folderNum, categoryName, categoryOutputDir) {
  const exercises = [];
  const files = await getPythonExerciseFiles(folder);

  for (const file of files) {
    const fileNum = file.match(PYTHON_FILE_PATTERN)[1];
    const exerciseId = `${parseInt(folderNum)}.${parseInt(fileNum)}`;
    const exerciseName = parseExerciseName(file, PYTHON_FILE_PATTERN);
    const sourcePath = join(ROOT_DIR, folder, file);
    const destPath = join(categoryOutputDir, file);
    const description = await extractPythonDescription(sourcePath);

    // Copy file to static folder
    await copyFile(sourcePath, destPath);

    exercises.push({
      id: exerciseId,
      name: exerciseName,
      runtime: 'python',
      category: categoryName,
      categoryFolder: folder,
      filename: file,
      path: `exercises/${folder}/${file}`,
      description
    });

    console.log(`  ${exerciseId} - [Python] ${exerciseName}`);
  }

  return exercises;
}

async function processSQLExercises(folder, folderNum, categoryName, categoryOutputDir) {
  const exercises = [];
  const files = await getSQLExerciseFiles(folder);

  for (const file of files) {
    const fileNum = file.match(SQL_FILE_PATTERN)[1];
    const exerciseId = `${parseInt(folderNum)}.${parseInt(fileNum)}`;
    const exerciseName = parseExerciseName(file, SQL_FILE_PATTERN);
    const sourcePath = join(ROOT_DIR, folder, file);
    const destPath = join(categoryOutputDir, file);
    const description = await extractSQLDescription(sourcePath);

    // Copy file to static folder
    await copyFile(sourcePath, destPath);

    exercises.push({
      id: exerciseId,
      name: exerciseName,
      runtime: 'sql',
      category: categoryName,
      categoryFolder: folder,
      filename: file,
      path: `exercises/${folder}/${file}`,
      description
    });

    console.log(`  ${exerciseId} - [SQL] ${exerciseName}`);
  }

  return exercises;
}

async function processReactExercises(folder, folderNum, categoryName, categoryOutputDir) {
  const exercises = [];
  const exerciseFolders = await getReactExerciseFolders(folder);

  for (const exerciseFolder of exerciseFolders) {
    const fileNum = exerciseFolder.match(REACT_FOLDER_PATTERN)[1];
    const exerciseId = `${parseInt(folderNum)}.${parseInt(fileNum)}`;
    const exerciseName = parseExerciseName(exerciseFolder, REACT_FOLDER_PATTERN);
    const sourcePath = join(ROOT_DIR, folder, exerciseFolder);
    const destPath = join(categoryOutputDir, exerciseFolder);
    const exerciseJsonPath = join(sourcePath, 'exercise.json');
    const description = await extractReactDescription(exerciseJsonPath);

    // Copy entire folder to static folder
    await cp(sourcePath, destPath, { recursive: true });

    exercises.push({
      id: exerciseId,
      name: exerciseName,
      runtime: 'react',
      category: categoryName,
      categoryFolder: folder,
      filename: exerciseFolder,
      path: `exercises/${folder}/${exerciseFolder}`,
      description
    });

    console.log(`  ${exerciseId} - [React] ${exerciseName}`);
  }

  return exercises;
}

async function main() {
  console.log('Building exercise manifest...\n');

  const exercises = [];
  const folders = await getExerciseFolders();

  // If no exercise folders found (e.g., on Vercel where only web/ is deployed),
  // skip regeneration - the static files are already committed
  if (folders.length === 0) {
    console.log('No exercise folders found in parent directory.');
    console.log('Using pre-committed static exercises.\n');
    return;
  }

  // Clean and recreate output directory
  if (existsSync(OUTPUT_DIR)) {
    await rm(OUTPUT_DIR, { recursive: true });
  }
  await mkdir(OUTPUT_DIR, { recursive: true });

  for (const folder of folders) {
    const folderNum = folder.match(FOLDER_PATTERN)[1];
    const categoryName = parseCategoryName(folder);
    const runtime = detectRuntime(folder);

    // Create category folder in output
    const categoryOutputDir = join(OUTPUT_DIR, folder);
    if (!existsSync(categoryOutputDir)) {
      await mkdir(categoryOutputDir, { recursive: true });
    }

    console.log(`\n${folder} (${runtime}):`);

    let folderExercises = [];

    switch (runtime) {
      case 'python':
        folderExercises = await processPythonExercises(folder, folderNum, categoryName, categoryOutputDir);
        break;
      case 'sql':
        folderExercises = await processSQLExercises(folder, folderNum, categoryName, categoryOutputDir);
        break;
      case 'react':
        folderExercises = await processReactExercises(folder, folderNum, categoryName, categoryOutputDir);
        break;
    }

    exercises.push(...folderExercises);
  }

  // Sort exercises by ID
  exercises.sort((a, b) => {
    const [aMajor, aMinor] = a.id.split('.').map(Number);
    const [bMajor, bMinor] = b.id.split('.').map(Number);
    return aMajor - bMajor || aMinor - bMinor;
  });

  // Write manifest
  const manifest = {
    generated: new Date().toISOString(),
    total: exercises.length,
    exercises
  };

  await writeFile(MANIFEST_PATH, JSON.stringify(manifest, null, 2));

  console.log(`\nGenerated manifest with ${exercises.length} exercises`);
  console.log(`Manifest: ${MANIFEST_PATH}`);
  console.log(`Exercises copied to: ${OUTPUT_DIR}`);
}

main().catch(console.error);
