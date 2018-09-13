
$("[id='filter_option']").change(function()
{
	if($(this).val() == "1"){
		$("[id='position_value']").show();
	} else {
		$("[id='position_value']").hide();
	}
	if($(this).val() == "2"){
		$("[id='salary_value']").show();
	} else {
		$("[id='salary_value']").hide();
	}
	if($(this).val() == "3"){
		$("[id='age_value']").show();
	} else {
		$("[id='age_value']").hide();
	}
	if($(this).val() == "4"){
		$("[id='gender_value']").show();
	} else {
		$("[id='gender_value']").hide();
	}
	if($(this).val() == "5"){
		$("[id='nationality_value']").show();
	} else {
		$("[id='nationality_value']").hide();
	}
	if($(this).val() == "6"){
		$("[id='status_value']").show();
	} else {
		$("[id='status_value']").hide();
	}
	if($(this).val() == "7"){
		$("[id='edu_value']").show();
	} else {
		$("[id='edu_value']").hide();
	}
	if($(this).val() == "8"){
		$("[id='university_value']").show();
	} else {
		$("[id='university_value']").hide();
	}
	if($(this).val() == "9"){
		$("[id='faculty_value']").show();
	} else {
		$("[id='faculty_value']").hide();
	}

});
$("[id='position_value']").hide();
$("[id='salary_value']").hide();
$("[id='age_value']").hide();
$("[id='gender_value']").hide();
$("[id='nationality_value']").hide();
$("[id='status_value']").hide();
$("[id='edu_value']").hide();
$("[id='university_value']").hide();
$("[id='faculty_value']").hide();
