#!/usr/bin/php

<?php
echo "Adding two n-bit binary integers, stored in two ";
echo "n-element arrays A and B.  The sum of the two integers ";
echo "should be stored in binary form in an (n+1)-element ";
echo "array C.\n";

$script = array_shift($argv);
echo "Usage: $script 000000 111111\n";

$len = count($argv);
$A = $argv[0];
$B = $argv[1];
$lenA = strlen($A);
$lenB = strlen($B);

$C = array();
if ($len == 2 && $lenA == $lenB)
{
	$upgrade = FALSE;
	for ($i = $lenA; $i > 0; $i--)
	{
		$sum = (int)($A[$i-1]) + (int)($B[$i-1]);
		if ($upgrade)
		{
			$sum += 1;
		}
		if ($sum > 1)
		{
			$upgrade = TRUE;
			$C[$i] = 0;
		}
		else
		{
			$upgrade = FALSE;
			$C[$i] = $sum;
		}
	}
	$C[0] = $upgrade ? 1 : 0;

	$lenC = $lenA + 1;
	for ($i = 0; $i < $lenC; $i++)
	{
		echo $C[$i];
	}
}

echo "\n";
