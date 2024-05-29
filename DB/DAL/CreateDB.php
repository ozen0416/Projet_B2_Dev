<?php
class CreateDB extends Service
{
  const NEEDED_ARGS = ["table", "params"];

  function Trig()
  {
    $db = new Database();
    // Tests if all NEEDED_ARGS were sent in the request
    if (!StdLib::testNeededArgs(self::NEEDED_ARGS, $this)) {
      return;
    }
    echo $db->create($this->{self::NEEDED_ARGS[0]}, $this->{self::NEEDED_ARGS[1]});
  }
}
