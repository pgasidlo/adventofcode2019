<?php

$ops = explode(",", file_get_contents("input.txt"));

/* ... before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. */
$ops[1] = 12;
$ops[2] = 2;

$i = 0;
$loop = true;
do {
  $op = $ops[$i++];
  print "i = {$i}, op = {$op}\n";
  if ($op == 99) {
    $loop = false;
    break;
  } elseif ($op == 1 || $op == 2) {
    $i1 = $ops[$i++];
    $i2 = $ops[$i++];
    $i3 = $ops[$i++];
    if ($op == 1) {
      $ops[$i3] = $v3 = (($v1 = $ops[$i1]) + ($v2 = $ops[$i2]));
    } else {
      $ops[$i3] = $v3 = (($v1 = $ops[$i1]) * ($v2 = $ops[$i2]));
    }
    print "v1({$i1}) = {$v1}, v2({$i2}) = {$v2}, v3({$i3}) = {$v3}\n";
  } else {
    throw Exception('invalid op');
  }
} while ($loop);

print "op[0] = {$ops[0]}";
