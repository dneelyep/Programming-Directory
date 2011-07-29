<?php /*Overriding a method and using the parent operator - in other words: if a
		class is using a certain method [test() in this case] that is also used
		by its child class, the child's statement will automatically be used rather
		than the parent's. However, if you want the parent's statement to be used,
		use the parent operator.*/

$object = new Son;
$object->test();
$object->test2();

class Dad
{
	function test()
	{
		echo "[Class Dad] I am your father<br />";
	}
}

class Son extends Dad
{
	function test()
	{
		echo "[Class Son] I am Luke<br />";
	}
	
	function test2()
	{
		parent::test(); //Here's the parent operator
	}
}
?>