<?php
class TestDB extends Service
{
  function Trig()
  {
    $arr = array("couleur", "feur", "jure");
    $formatArr = Format::ArrRefactor($arr, "WHERE ", "`%s`", "FEUR");
    echo $formatArr;
  }
}
