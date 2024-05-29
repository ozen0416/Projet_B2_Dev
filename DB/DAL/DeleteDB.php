<?php
class DeleteDB extends Service
{
  const NEEDED_ARGS = ["table", "filter"];
  function Trig()
  {
    $db = new Database();
    // Tests if all NEEDED_ARGS were sent in the request
    if (!StdLib::testNeededArgs(self::NEEDED_ARGS, $this)) {
      return;
    }

    // Line seems funky
    echo $db->delete($this->{self::NEEDED_ARGS[0]}, $this->{self::NEEDED_ARGS[1]});
  }
}
