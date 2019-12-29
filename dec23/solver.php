<?php

$alphabets = array(
	0 => "abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ23456789",
	1 => "abcdefghijkmpqrstuvwxyz23456789ABCDEFGHJKLMPQRSTUVWXYZ",
	2 => "23456789ABCDEFGHJKLMPQRSTUVWXYZabcdefghijkmpqrstuvwxyz",
	3 => "23456789abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ",
	4 => "ABCDEFGHJKLMPQRSTUVWXYZabcdefghijkmpqrstuvwxyz23456789",
	5 => "ABCDEFGHJKLMPQRSTUVWXYZ23456789abcdefghijkmpqrstuvwxyz"
);

function generateString($seed, $alphabet)
{
	srand($seed);

	$pwd = "";
	for ($j=0; $j < 12; $j++) { 
		$val = rand(0,strlen($alphabet)-1);
		$pwd .= $alphabet[$val];
	}
	
	fwrite(STDERR, "" . $seed . " " . $alphabet . " " . $pwd . "\n");
	print($pwd);
	print("\n")
}

$start = 0;
$start = 3043530;
for ($i=$start; $i < PHP_INT_MAX; $i++) { 

	fwrite(STDERR, "$i\n");
	for ($a=0; $a < sizeof($alphabets); $a++) { 

		generateString($i, $alphabets[$a]);
	}
}

?>
