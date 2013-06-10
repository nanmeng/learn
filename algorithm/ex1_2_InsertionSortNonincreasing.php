#!/usr/bin/php

<?php
echo "Rewrite INSERTION-SORT procedure to sort ";
echo "into nonincreasing instead of nondecreasing order\n";

$script = array_shift($argv);
echo "Usage: $script 2 4 5 1 9\n";

$len = count($argv);
if ($len > 0)
{
	for ($i = 1; $i < $len; $i++)
	{
		$key = $argv[$i];
		$j = $i - 1;
		while ($j >= 0 && $argv[$j] < $key)
		{
			$argv[$j+1] = $argv[$j];
			$j--;
		}
		$argv[$j+1] = $key;
	}

	print_r($argv);
}
