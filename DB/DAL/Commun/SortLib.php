<?php
class SortLib
{
  static function BubbleSortRecursive($arr, $indexOfLastElem)
  {
    if (gettype($arr) != "array") {
      return "Error: wrong type value";
    }
    // Test if array is only one element
    if ($indexOfLastElem <= 1) {
      return $arr;
    } else {
      for ($i = 1; $i < $indexOfLastElem; $i++) {
        if ($arr[$i - 1] > $arr[$i]) {
          $tmp = $arr[$i - 1];
          $arr[$i - 1] = $arr[$i];
          $arr[$i] = $tmp;
        }
      }
      // recalls the function ignoring the last element
      return self::BubbleSortRecursive($arr, $indexOfLastElem - 1);
    }
  }

  static function MergeSort($arr)
  {
    if (gettype($arr) != "array") {
      return "Error: Wrong type value";
    }
    $size = count($arr);
    // Base case of the recursion
    // if the array is only one item, return the item
    if ($size <= 1) {
      return $arr;
    }

    $tmp = $arr[0];
    $left = array();
    $right = array();
    for ($i = 1; $i < $size; $i++) {
      if ($arr[$i] < $tmp) {
        $left[] = $arr[$i];
      } else {
        $right[] = $arr[$i];
      }
    }
    return array_merge(self::MergeSort($left), array($tmp), self::MergeSort($right));
  }


  static function DumpArray($arr)
  {
    if (gettype($arr) != "array") {
      echo "Error: wrong type value";
      return;
    }
    for ($i = 0; $i < count($arr); $i++) {
      if ($i != count($arr) - 1) {
        echo $arr[$i] . ", ";
      } else {
        echo $arr[$i] . " ";
      }
    }
    echo "\n";
  }
}
