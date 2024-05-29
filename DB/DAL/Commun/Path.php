<?php
class Path
{
  static function PATH($file = "")
  {
    return $_SERVER["DOCUMENT_ROOT"] . "/" . $file;
  }

  static function SECURE_PATH($file = "")
  {
    return self::PATH() . "../" . $file;
  }

  static function CREDENTIALS($file = "")
  {
    return self::SECURE_PATH() . "credentials/" . $file;
  }
}
