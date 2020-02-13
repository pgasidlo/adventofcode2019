<?php

$masses = array_map('trim', file("input.txt"));
$total_fuel = 0;
foreach ($masses as $mass) {
  $fuel = floor($mass / 3.0) - 2;
  $total_fuel += $fuel;
}
print "Result: {$total_fuel}\n";

