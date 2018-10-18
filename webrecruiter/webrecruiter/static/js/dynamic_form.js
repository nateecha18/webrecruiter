$(document).ready(function(){
  var i=1;
  $('#add_hisedu').click(function(){
    i++;
    var j=i+1;
    var append_text = '';

    // Head (Filter Select + Add More button)
    append_text += '<div class="form-content" id="'+i+'" class="his_edu"><div class="row"><div class="col-md-12"><div class="col-sm-5 col-sm-offset-1"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">school</i> </span><div class="form-group label-floating"> <label class="control-label">ประเภทการศึกษา (Education Level)</label> <select name="edu_level" class="form-control"> {% for level in Levels %} {% if level.value == \'level_bacDe\' %}<option value="{{ level.value }}" selected>{{ level.education_level }}</option> {% else %}<option value="{{ level.value }}">{{ level.education_level }}</option> {% endif %} {% endfor %} </select></div></div></div>';
    append_text += '<div class="col-sm-5"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">public</i> </span><div class="form-group label-floating"> <label class="control-label">ประเทศที่จบ (Country)</label> <select name="edu_country" class="form-control"> {% for country in Country %} {% if country.countryName == \'Thailand\' %}<option value="{{ country.countryName }}" selected>{{ country.countryName }}</option> {% else %}<option value="{{ country.countryName }}">{{ country.countryName }}</option> {% endif %} {% endfor %} </select></div></div></div>';
    append_text += '<div class="col-sm-10 col-sm-offset-1"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">school</i> </span><div class="form-group label-floating"> <label class="control-label">ชื่อสถานศึกษา (Institute Name)</label> <input type="text" class="form-control" name="edu_instituteName" id="institute'+j+'"></div></div></div>';
    append_text += '<div class="col-sm-5 col-sm-offset-1"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">calendar_today</i> </span><div class="form-group label-floating"> <label class="control-label">ตั้งแต่ปี (From)</label> <select name="edu_fromYear" class="form-control"><option disabled="" selected=""></option><option value="2018">2018</option><option value="2017">2017</option><option value="2016">2016</option><option value="2015">2015</option><option value="2014">2014</option><option value="2013">2013</option><option value="2012">2012</option><option value="2011">2011</option><option value="2010">2010</option><option value="2009">2009</option><option value="2008">2008</option><option value="2007">2007</option><option value="2006">2006</option><option value="2005">2005</option><option value="2004">2004</option><option value="2003">2003</option><option value="2002">2002</option><option value="2001">2001</option>';
    append_text += '<option value="2000">2000</option><option value="1999">1999</option><option value="1998">1998</option><option value="1997">1997</option><option value="1996">1996</option><option value="1995">1995</option><option value="1994">1994</option><option value="1993">1993</option><option value="1992">1992</option><option value="1991">1991</option><option value="1990">1990</option><option value="1989">1989</option><option value="1988">1988</option><option value="1987">1987</option><option value="1986">1986</option><option value="1985">1985</option><option value="1984">1984</option><option value="1983">1983</option><option value="1982">1982</option><option value="1981">1981</option><option value="1980">1980</option><option value="1979">1979</option><option value="1978">1978</option><option value="1977">1977</option><option value="1976">1976</option><option value="1975">1975</option><option value="1974">1974</option><option value="1973">1973</option>';
    append_text += '<option value="1972">1972</option><option value="1971">1971</option><option value="1970">1970</option><option value="1969">1969</option><option value="1968">1968</option> </select></div></div></div>';
    append_text += '<div class="col-sm-5"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">calendar_today</i> </span><div class="form-group label-floating"> <label class="control-label">ถึงปี (To)</label> <select name="edu_toYear" class="form-control"><option disabled="" selected=""></option><option value="2018">2018</option><option value="2017">2017</option><option value="2016">2016</option><option value="2015">2015</option><option value="2014">2014</option><option value="2013">2013</option><option value="2012">2012</option><option value="2011">2011</option><option value="2010">2010</option><option value="2009">2009</option><option value="2008">2008</option><option value="2007">2007</option><option value="2006">2006</option><option value="2005">2005</option><option value="2004">2004</option><option value="2003">2003</option><option value="2002">2002</option><option value="2001">2001</option><option value="2000">2000</option>';
    append_text += '<option value="1999">1999</option><option value="1998">1998</option><option value="1997">1997</option><option value="1996">1996</option><option value="1995">1995</option><option value="1994">1994</option><option value="1993">1993</option><option value="1992">1992</option><option value="1991">1991</option><option value="1990">1990</option><option value="1989">1989</option><option value="1988">1988</option><option value="1987">1987</option><option value="1986">1986</option><option value="1985">1985</option><option value="1984">1984</option><option value="1983">1983</option><option value="1982">1982</option><option value="1981">1981</option><option value="1980">1980</option><option value="1979">1979</option><option value="1978">1978</option><option value="1977">1977</option><option value="1976">1976</option><option value="1975">1975</option><option value="1974">1974</option><option value="1973">1973</option><option value="1972">1972</option>';
    append_text += '<option value="1971">1971</option><option value="1970">1970</option><option value="1969">1969</option><option value="1968">1968</option> </select></div></div></div>';
    append_text += '<div class="col-sm-5 col-sm-offset-1"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">extension</i> </span><div class="form-group label-floating"> <label class="control-label">สาขาวิชา (Major Subject)</label> <input name="edu_major" type="text" class="form-control"></div></div></div><div class="col-sm-5"><div class="input-group"> <span class="input-group-addon"> <i class="material-icons">equalizer</i> </span><div class="form-group label-floating"> <label class="control-label">เกรดเฉลี่ย (GPA)</label> <input name="edu_gpa" type="text" class="form-control"></div></div></div>';
    append_text += '</div><div class="col-md-12 text-center"><div class="form-group"><div class="col-md-12"> <button type="button" id="'+i+'" class="btn btn-simple btn-xs btn_hisedu_remove"><i class="material-icons md-18 icon-delete">delete</i></button></div></div></div>';


    $('#history_education_form').append(append_text);
    $( "#institute"+j ).each(function(){
      $(this).autocomplete({
        source: "{% url 'get_institute' %}",
        minLength: 1,
      });
    });

  });

  // Remove w/ Jquery Style
  $(document).on('click', '.btn_hisedu_remove', function(){
    var button_id = $(this).attr("id");
    $.confirm({
      title: 'Delete this History Education ?!',
      content: "คุณต้องการลบประวัติการศึกษานี้หรือไม่?",
      buttons: {
        ใช่: function(){
          $('#'+button_id+'').remove();
        },
        ไม่ใช่: function(){
        }
      }
    });
  });
});
