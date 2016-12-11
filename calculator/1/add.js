/**
 * Created by Sherry on 2016/9/29.
 */
function add()
{
    var adder1=Number(document.form1.myadder1.value);
    var adder2=Number(document.form1.myadder2.value);
    var result=adder1+adder2;
    //alert(result)
    document.form1.myresult.value=result;
}