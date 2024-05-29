<?php
class ReadDB extends Service
{
  const NEEDED_ARGS = ["table", "columns"];
  const OPTIONAL_ARG = "filter";
  function Trig()
  {
    $db = new Database();
    // Tests if all NEEDED_ARGS were sent in the request
    if (!StdLib::testNeededArgs(self::NEEDED_ARGS, $this)) {
      return;
    }

    // Tests if there are filters
    // Seems funky
    if (isset($this->{self::OPTIONAL_ARG})) {
      echo $db->read($this->{self::NEEDED_ARGS[0]}, $this->{self::NEEDED_ARGS[1]}, $this->{self::OPTIONAL_ARG});
    } else {
      echo $db->read($this->{self::NEEDED_ARGS[0]}, $this->{self::NEEDED_ARGS[1]});
    }
  }
}
