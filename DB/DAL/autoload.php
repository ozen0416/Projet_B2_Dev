<?php

/**
 * Simple autoloader
 *
 * @param $class_name - String name for the class that is trying to be loaded.
 */
function my_custom_autoloader($className)
{
  // Define an array of directories to search for class files
  $directories = [
    __DIR__ . '/',
    __DIR__ . '/Commun/'
  ];

  // Iterate through the directories
  foreach ($directories as $directory) {
    // Construct the file path
    $file = $directory . $className . '.php';

    // If the file exists, require it
    if (file_exists($file)) {
      require_once $file;
      return;
    }
  }
}
// add a new autoloader by passing a callable into spl_autoload_register()
spl_autoload_register('my_custom_autoloader');
