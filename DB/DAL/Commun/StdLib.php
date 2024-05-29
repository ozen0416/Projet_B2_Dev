<?php
class StdLib
{
  static function testNeededArgs($arrOfArgs, $classInstance)
  {
    foreach ($arrOfArgs as $arg) {
      if (!isset($classInstance->{$arg})) {
        echo json_encode(['error' => 'Missing ' . $arg . ' in JSON data']);
        return false;
      }
    }
    return true;
  }

  static function className($currDir = "")
  {
    // Refactor the string to match the class name
    $dirPath = str_replace("/index.php", "", $_SERVER['SCRIPT_NAME']);
    $filePath = str_replace($currDir, "", $dirPath);

    return str_replace("/", "", $filePath);
  }
}
