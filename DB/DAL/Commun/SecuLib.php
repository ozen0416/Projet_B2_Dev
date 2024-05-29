<?php
class SecuLib
{
  public static function getCredentials($file)
  {
    $json = file_get_contents(Path::CREDENTIALS($file));
    return json_decode($json);
  }
}
