<?php
class UpdateDB extends Service
{
  const NEEDED_ARGS = ["table", "params", "filter"];
  function Trig()
  {
    $db = new Database();
    // Tests if all NEEDED_ARGS were sent in the request
    if (!StdLib::testNeededArgs(self::NEEDED_ARGS, $this)) {
      return;
    }
    echo $db->update($this->{self::NEEDED_ARGS[0]}, $this->{self::NEEDED_ARGS[1]}, $this->{self::NEEDED_ARGS[2]});
  }
}
