<?php
class Format
{
  static function ArrRefactor($arr, $prefix = "", $dataType = "`%s`", $suffix = "", $sep = ",")
  {
    $format = $dataType . $sep;
    $startFormat = $prefix . $dataType . $sep;
    $endFormat = $dataType . $suffix;
    $formattedArr = "";

    // Add prefix only on first element of list
    $formattedArr .= sprintf($startFormat, $arr[0]);
    for ($i = 1; $i < count($arr) - 1; $i++) {
      // format the key of the array
      $formattedArr .= sprintf($format, ($arr[$i]));
    }
    // Do not add the separator after the last element 
    $formattedArr .= sprintf($endFormat, $arr[count($arr) - 1]);
    return $formattedArr;
  }
}
