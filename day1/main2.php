<?php

$masses = array_map('trim', file("input.txt"));
$total_fuel = 0;
foreach ($masses as $mass) {

  $fuel = floor($mass / 3.0) - 2;
  $total_fuel += $fuel;

  $loop = true;
  do {
    $fuel = floor($fuel / 3.0) - 2;
    if ($fuel <= 0) {
      $loop = false;
      break;
    }
    $total_fuel += $fuel;
  } while ($loop);

}
print "Result: {$total_fuel}\n";

