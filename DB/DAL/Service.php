<?php
abstract class Service
{

  const ALLOWED_ARGS = ["table", "params", "columns", "filter"];

  function __construct()
  {
    if ($_SERVER["REQUEST_METHOD"] != "POST") {
      http_response_code(405);
      echo json_encode(['error' => 'Method Not Allowed']);
      return;
    }

    $jsonData = json_decode(file_get_contents('php://input'), true);

    if ($jsonData == null) {
      http_response_code(400);
      echo json_encode(['error' => 'Invalid JSON data']);
      return;
    }

    foreach ($jsonData as $attribute => $value) {
      // Only set variables that are in ALLOWED_ARGS
      if (in_array($attribute, self::ALLOWED_ARGS)) {
        $this->{$attribute} = $value;
      }
    }

    // Only calls Trig if JSON data was sent
    static::Trig();
  }
  abstract function Trig();
}
