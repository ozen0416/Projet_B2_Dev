<?php

use PDO;

class Connection
{
  static $instance;
  static function Connect($file = NULL)
  {
    if (!isset(self::$instance)) {
      // Get default DB credentials
      if ($file == NULL) {
        $file = "db.json";
      }
      $cred = SecuLib::getCredentials($file);
      //TODO change db name
      self::$instance = new PDO('mysql:host=localhost;dbname=' . $cred->dbName, $cred->login, $cred->password);
    }
    return self::$instance;
  }
}
