/**
 * Build script to generate exercise manifest and copy exercise files
 * Run with: node scripts/build-exercises.js
 */

import { readdir, readFile, writeFile, mkdir, copyFile, rm } from 'fs/promises';
import { existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = join(__dirname, '..', '..');
const OUTPUT_DIR = join(__dirname, '..', 'static', 'exercises');
const MANIFEST_PATH = join(__dirname, '..', 'src', 'lib', 'exercises-manifest.json');

// Exercise folder pattern: NN-category-name
const FOLDER_PATTERN = /^(\d{2})-(.+)$/;
// Exercise file pattern: NN_exercise_name.py
const FILE_PATTERN = /^(\d{2})_(.+)\.py$/;

async function getExerciseFolders() {
  const entries = await readdir(ROOT_DIR, { withFileTypes: true });
  return entries
    .filter(entry => entry.isDirectory() && FOLDER_PATTERN.test(entry.name))
    .map(entry => entry.name)
    .sort();
}

async function getExerciseFiles(folder) {
  const folderPath = join(ROOT_DIR, folder);
  const entries = await readdir(folderPath, { withFileTypes: true });
  return entries
    .filter(entry => entry.isFile() && FILE_PATTERN.test(entry.name))
    .map(entry => entry.name)
    .sort();
}

function parseExerciseName(filename) {
  // Convert 01_variables_and_types.py -> Variables And Types
  const match = filename.match(FILE_PATTERN);
  if (!match) return filename;
  return match[2]
    .split('_')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function parseCategoryName(folder) {
  // Convert 01-basics -> Basics
  const match = folder.match(FOLDER_PATTERN);
  if (!match) return folder;
  return match[2]
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

async function extractDescription(filePath) {
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
    const files = await getExerciseFiles(folder);

    // Create category folder in output
    const categoryOutputDir = join(OUTPUT_DIR, folder);
    if (!existsSync(categoryOutputDir)) {
      await mkdir(categoryOutputDir, { recursive: true });
    }

    for (const file of files) {
      const fileNum = file.match(FILE_PATTERN)[1];
      const exerciseId = `${parseInt(folderNum)}.${parseInt(fileNum)}`;
      const exerciseName = parseExerciseName(file);
      const sourcePath = join(ROOT_DIR, folder, file);
      const destPath = join(categoryOutputDir, file);
      const description = await extractDescription(sourcePath);

      // Copy file to static folder
      await copyFile(sourcePath, destPath);

      exercises.push({
        id: exerciseId,
        name: exerciseName,
        category: categoryName,
        categoryFolder: folder,
        filename: file,
        path: `exercises/${folder}/${file}`,
        description
      });

      console.log(`  ${exerciseId} - ${exerciseName}`);
    }
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
