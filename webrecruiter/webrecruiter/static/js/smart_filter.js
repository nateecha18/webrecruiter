$(document).ready(function(){
  var i=1;
  $('#add').click(function(){
    i++;
    var append_text = '';

    // Head (Filter Select + Add More button)
    append_text = '<div id="'+i+'" class="filter_list"> <div class="row"> <div class="col-lg-4"> <div class="col-lg-2 text-center"> <span class="number_circle">'+i+'</span> </div><div class="col-lg-10"> <select class="form-control" name="filter_option" id="filter_option'+i+'"> <option selected value="0">Select a filter</option> <option value="1">ตำแหน่ง</option> <option value="2">เงินเดือน</option> <option value="3">อายุ</option> <option value="4">เพศ</option> <option value="5">สัญชาติ</option> <option value="6">สถานภาพ</option> <option value="7">สถานะการศึกษาปัจจุบัน</option> <option value="8">มหาวิทยาลัย</option> <option value="9">คณะ</option> <option value="10">สาขาวิชา</option> <option value="11">เกรดเฉลี่ย</option> <option value="12">ความสามารถด้านคอมพิวเตอร์</option> <option value="13">ความสามารถด้านภาษา</option> <option value="14">การอบรม ประกาศนียบัตร และ รางวัล</option> <option value="15">ประสบการณ์ทำงาน ฝึกงาน</option> </select> </div></div>';
    // Detaill Input field
    append_text += ' <div class="col-lg-7" id="position_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px;" name="operator_position"> <option selected="" disabled value="0">Operator Position</option> <option value="1">ตำแหน่ง (is)</option> <option value="2">ไม่ใช่ตำแหน่ง (isnot)</option> <option value="3">ตำแหน่งที่มี (contains)</option> <option value="4">ตำแหน่งที่ไม่มี (isnot contains)</option> </select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="ตำแหน่ง" name="filter_position"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="salary_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_salary"> <option selected="" disabled value="0">Operator Salary</option> <option value="1">เท่ากับ (=)</option> <option value="2">มากกว่าเท่ากับ (>=)</option> <option value="3">น้อยกว่าเท่ากับ (<=)</option> <option value="4">มากกว่า (>)</option> <option value="5">น้อยกว่า (<)</option> <option value="6">ระหว่าง (Between)</option> </select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="เงินเดือน" name="filter_salary"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="age_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_age"> <option selected="" disabled value="0">Operator Age</option> <option value="1">เท่ากับ (=)</option> <option value="2">มากกว่าเท่ากับ (>=)</option> <option value="3">น้อยกว่าเท่ากับ (<=)</option> <option value="4">มากกว่า (>)</option> <option value="5">น้อยกว่า (<)</option> <option value="6">ระหว่าง (Between)</option> </select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="อายุ" name="filter_age"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="gender_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_gender"> <option selected="" disabled value="0">Operator Gender</option> <option value="1">เพศ (is)</option> <option value="2">ไม่เอาเพศ (isnot)</option> </select> </div><div class="col-lg-8"> <select class="form-control" style="margin-top:0px" name="filter_gender"> <option selected="" hidden value="0">--- เลือกเพศ ---</option> <option value="m">ชาย (Men)</option> <option value="w">หญิง (Women)</option> </select> </div></div>';
    append_text += ' <div class="col-lg-7" id="nationality_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_nationality"> <option selected="" disabled value="0">Operator Nationality</option> <option value="1">สัญชาติ (is)</option> <option value="2">ไม่เอาสัญชาติ (isnot)</option> <option value="3">สัญชาติที่เป็น (contains)</option> <option value="4">สัญชาติที่ไม่เป็น (isnot contains)</option> </select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="สัญชาติ" name="filter_nationality"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="status_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_status"> <option selected="" disabled value="0">Operator Status</option> <option value="1">สถานภาพ (is)</option> <option value="2">ไม่เอาสถานภาพ (isnot)</option> </select> </div><div class="col-lg-8"> <select class="form-control" style="margin-top:0px" name="filter_status"> <option selected="" hidden value="0">--- เลือกสถานภาพ ---</option> <option value="โสด">โสด (Single)</option> <option value="สมรส">สมรส (Married)</option> <option value="หม้าย">หม้าย (Widowed)</option> <option value="หย่า">หย่า (Divorced)</option> </select> </div></div>';
    append_text += ' <div class="col-lg-7" id="edu_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_edu"> <option selected="" disabled value="0">--- เลือกสถานะการศึกษา ---</option> <option value="1">อยู่ระหว่างการศึกษา</option> <option value="2">สำเร็จการศึกษาแล้ว</option> </select> </div><div class="col-lg-8"> <p> </p></div></div>';
    append_text += ' <div class="col-lg-7" id="university_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_university"> <option selected="" disabled value="0">Operator University</option> <option value="1">มหาวิทยาลัย (is)</option> <option value="2">ไม่เอามหาวิทยาลัย (isnot)</option> <option value="3">มหาวิทยาลัยที่เป็น (contains)</option> <option value="4">มหาวิทยาลัยที่ไม่เป็น (isnot contains)</option> </select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="มหาวิทยาลัย" name="filter_university"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="faculty_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_faculty"> <option selected="" disabled value="0">Operator Faculty</option> <option value="1">คณะ (is)</option> <option value="2">ไม่เอาคณะ (isnot)</option> <option value="3">คณะที่เป็น (contains)</option> <option value="4">คณะที่ไม่เป็น (isnot contains)</option> </select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="คณะ" name="filter_faculty"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="gpa_value'+i+'"> <div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_gpa"> <option selected="" disabled value="0">Operator GPA</option><option value="1">เท่ากับ (=)</option><option value="2">มากกว่าเท่ากับ (>=)</option><option value="3">น้อยกว่าเท่ากับ (<=)</option><option value="4">มากกว่า (>)</option><option value="5">น้อยกว่า (<)</option></select> </div><div class="col-lg-8"> <div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="เกรดเฉลี่ย" name="filter_gpa"> </div></div></div>';
    append_text += ' <div class="col-lg-7" id="comskill_value'+i+'"><div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_comskill"><option selected="" disabled value="0">Operator Computer Skill</option><option value="1">ทักษะ (is)</option><option value="2">ไม่เอาทักษะ (isnot)</option><option value="3">ทักษะที่มี (contains)</option><option value="4">ทักษะที่ไม่มี (isnot contains)</option> </select></div><div class="col-lg-8"><div class="form-group"><div rel="tooltip" title="กรอกเฉพาะ keyword สำคัญ เช่น python , css , troupleshoot"> <input name="tags'+i+'" class="" id="tags" placeholder="กรอกความสามารถด้านคอมพิวเตอร์ที่ต้องการ" value="" autofocus></div></div></div></div>';
    append_text += ' <div class="col-lg-7" id="major_value'+i+'"><div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_major"><option selected="" disabled value="0">Operator Major</option><option value="1">สาขา (is)</option><option value="2">ไม่เอาสาขา (isnot)</option><option value="3">สาขาที่เป็น (contains)</option><option value="4">สาขาที่ไม่เป็น (isnot contains)</option> </select></div><div class="col-lg-8"><div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="สาขาวิชา" name="filter_major"></div></div></div>';
    append_text += '<div class="col-lg-7" id="language_value'+i+'"><div class="col-lg-6"> <select class="form-control" style="margin-top:0px" name="operator_language"><option selected="" disabled value="0">Operator Language</option><option value="1">มีความสามารถด้านภาษา (is)</option><option value="2">ไม่เอาผู้ที่มีความสามารถด้านภาษา (isnot)</option> </select></div><div class="col-lg-6"> <select class="form-control" style="margin-top:0px" name="filter_language"><option selected="" hidden value="0">--- เลือกภาษา ---</option><option value="ไทย" is-active="1">ไทย</option><option value="อังกฤษ" is-active="1">อังกฤษ</option><option value="ญี่ปุ่น" is-active="1">ญี่ปุ่น</option><option value="จีน" is-active="0">จีน</option><option value="มาเลเซีย" is-active="1">มาเลเซีย</option><option value="เกาหลี" is-active="1">เกาหลี</option><option value="เขมร" is-active="1">เขมร</option><option value="เดนมาร์ก" is-active="1">เดนมาร์ก</option><option value="เยอรมัน" is-active="1">เยอรมัน</option>';
    append_text += '<option value="ฝรั่งเศส" is-active="1">ฝรั่งเศส</option><option value="ลาว" is-active="1">ลาว</option><option value="สเปน" is-active="1">สเปน</option><option value="อิตาลี" is-active="1">อิตาลี</option><option value="จีน" is-active="1">จีน</option><option value="รัสเซีย" is-active="1">รัสเซีย</option> </select></div></div>';
    append_text += '<div class="col-lg-7" id="experience_value'+i+'"><div class="col-lg-4"> <select class="form-control" style="margin-top:0px" name="operator_experience"><option selected="" disabled value="0">Operator Experience</option><option value="1">ประสบการณ์ (is)</option><option value="2">ไม่เอาประสบการณ์ (isnot)</option><option value="3">ประสบการณ์ที่เป็น (contains)</option><option value="4">ประสบการณ์ที่ไม่เป็น (isnot contains)</option> </select></div><div class="col-lg-8"><div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="ประสบการณ์" name="filter_experience"></div></div></div>';
    append_text += '<div class="col-lg-7" id="workexp_value'+i+'"><div class="col-lg-5"> <select class="form-control" style="margin-top:0px;" name="operator_workexp"><option selected="" disabled value="0">Operator Position Experience</option><option value="1">ประสบการณ์ตำแหน่ง (is)</option><option value="2">ไม่ใช่ประสบการณ์ตำแหน่ง (isnot)</option><option value="3">ประสบการณ์ตำแหน่งที่มี (contains)</option><option value="4">ประสบการณ์ตำแหน่งที่ไม่มี (isnot contains)</option> </select></div><div class="col-lg-7"><div class="form-group"> <input class="form-control" style="border-radius:5px;height:40px;margin-top:0px;" type="text" placeholder="ประสบการณ์การทำงานตำแหน่ง" name="filter_workexp"></div></div></div>';
    // Other Detail here!
    // End (Delete button)
    append_text += ' <div class="col-lg-1"> <div class="text-center" style="margin-top: 8px;"> <button type="button" id="'+i+'" class="btn btn-simple btn-xs btn_remove"><i class="material-icons md-18 icon-delete">delete</i></button> </div></div></div></div>';



    $('#filter').append(append_text);

    $('#position_value'+i+'').hide();
    $('#salary_value'+i+'').hide();
    $('#age_value'+i+'').hide();
    $('#gender_value'+i+'').hide();
    $('#nationality_value'+i+'').hide();
    $('#status_value'+i+'').hide();
    $('#edu_value'+i+'').hide();
    $('#university_value'+i+'').hide();
    $('#faculty_value'+i+'').hide();
    $('#gpa_value'+i+'').hide();
    $('#comskill_value'+i+'').hide();
    $('#major_value'+i+'').hide();
    $('#language_value'+i+'').hide();
    $('#experience_value'+i+'').hide();
    $('#workexp_value'+i+'').hide();


    $('#tags').each(function(){
      var list = ['Adobe Campaign', ' Data analytics', ' Excel', ' FileMaker Pro', ' Fortran', ' Hive', ' HQL', ' MATLAB', ' Microsoft Access', ' Microsoft Excel', ' Numeracy', " Object oriented database management systems' (OODBMS)", ' QuickBooks', ' Relational database management systems (RDBMS)', ' SAS', ' Spark', ' SPSS', ' Statistics', ' XML database management systems', ' Backup management', ' Client server management', ' Client support', ' Configuration', ' Diagnostics', ' End user support', ' Help desk', ' Implementation', ' Installation', ' Issue tracking systems (ITS)', ' Networking', ' Support', ' Systems administration', ' Tech support', ' Troubleshooting','Adobe Creative Cloud', ' Adobe Illustrator', ' Adobe InDesign', ' Adobe Photoshop', ' APIs', ' Art design', ' AutoCAD', ' CorelDRAW', ' Corel WordPerfect', ' Design', ' Desktop publishing', ' InDesign', ' Integrating interactive elements with websites', ' Maya', ' Microsoft Outlook', ' Microsoft Publisher', ' Microsoft Visual Studio', ' Microsoft Word', ' Operating digital video cameras', ' Presentations', ' Typing','Build automation software', ' C', ' C++', ' CISC and RISC architecture', ' Embedded processor hardware design', ' Field-programmable gate array (FPGA) development tools', ' Hardware description language (HDL)', ' Hardware verification tools and techniques', ' HTML', ' Integrated development environments', ' Java', ' LabVIEW', ' Linux', ' Memory management', ' Open-source software (OSS)', ' PCB layout review', ' Python', ' SQL', ' UI/UX', ' Unix', ' Windows Shell', ' XML',"A# .NET", "A# (Axiom)", "A-0 System", "A+", "A++", "ABAP", "ABC", "ABC ALGOL", "ABSET", "ABSYS", "ACC", "Accent", "Ace DASL", "ACL2", "Avicsoft", "ACT-III", "Action!", "ActionScript", "Ada", "Adenine", "Agda", "Agilent VEE", "Agora", "AIMMS", "Alef", "ALF", "ALGOL 58", "ALGOL 60", "ALGOL 68", "ALGOL W", "Alice", "Alma-0", "AmbientTalk", "Amiga E", "AMOS", "AMPL", "Apex (Salesforce.com)", "APL", "AppleScript", "Arc", "ARexx", "Argus", "AspectJ", "Assembly language", "ATS", "Ateji PX", "AutoHotkey", "Autocoder", "AutoIt", "AutoLISP / Visual LISP", "Averest", "AWK", "Axum", "Active Server Pages", "ASP.NET", "B", "Babbage", "Bash", "BASIC", "bc", "BCPL", "BeanShell", "Batch (Windows/Dos)", "Bertrand", "BETA", "Bigwig", "Bistro", "BitC", "BLISS", "Blockly", "BlooP", "Blue", "Boo", "Boomerang", "Bourne shell (including bash and ksh)", "BREW", "BPEL", "B", "C--", "C++ – ISO/IEC 14882", "C# – ISO/IEC 23270", "C/AL", "Caché ObjectScript", "C Shell", "Caml", "Cayenne", "CDuce", "Cecil", "Cesil", "Céu", "Ceylon", "CFEngine", "CFML", "Cg", "Ch", "Chapel", "Charity", "Charm", "Chef", "CHILL", "CHIP-8", "chomski", "ChucK", "CICS", "Cilk", "Citrine (programming language)", "CL (IBM)", "Claire", "Clarion", "Clean", "Clipper", "CLIPS", "CLIST", "Clojure", "CLU", "CMS-2", "COBOL – ISO/IEC 1989", "CobolScript – COBOL Scripting language", "Cobra", "CODE", "CoffeeScript", "ColdFusion", "COMAL", "Combined Programming Language (CPL)", "COMIT", "Common Intermediate Language (CIL)", "Common Lisp (also known as CL)", "COMPASS", "Component Pascal", "Constraint Handling Rules (CHR)", "COMTRAN", "Converge", "Cool", "Coq", "Coral 66", "Corn", "CorVision", "COWSEL", "CPL", "CPL", "Cryptol", "csh", "Csound", "CSP", "CUDA", "Curl", "Curry", "Cybil", "Cyclone", "Cython", "M2001", "M4", "M#", "Machine code", "MAD (Michigan Algorithm Decoder)", "MAD/I", "Magik", "Magma", "make", "Maple", "MAPPER now part of BIS", "MARK-IV now VISION:BUILDER", "Mary", "MASM Microsoft Assembly x86", "MATH-MATIC", "Mathematica", "MATLAB", "Maxima (see also Macsyma)", "Max (Max Msp – Graphical Programming Environment)", "MaxScript internal language 3D Studio Max", "Maya (MEL)", "MDL", "Mercury", "Mesa", "Metafont", "Microcode", "MicroScript", "MIIS", "Milk (programming language)", "MIMIC", "Mirah", "Miranda", "MIVA Script", "ML", "Model 204", "Modelica", "Modula", "Modula-2", "Modula-3", "Mohol", "MOO", "Mortran", "Mouse", "MPD", "Mathcad", "MSIL – deprecated name for CIL", "MSL", "MUMPS", "Mystic Programming L"]
      var input = document.querySelector("input[name=tags"+i+"]"),
      // init Tagify script on the above inputs
      tagify = new Tagify(input, {
        whitelist : list,
        blacklist : ["react", "angular"]
      });

      // "remove all tags" button event listener
      document.querySelector(".tags--removeAllBtn")
      .addEventListener("click", tagify.removeAllTags.bind(tagify))

      // Chainable event listeners
      tagify.on("add", onAddTag)
      .on("remove", onRemoveTag)
      .on("invalid", onInvalidTag);

      // tag added callback
      function onAddTag(e){
        console.log(e, e.detail);
        console.log( tagify.DOM.originalInput.value )
        tagify.off("add", onAddTag) // exmaple of removing a custom Tagify event
      }

      // tag remvoed callback
      function onRemoveTag(e){
        console.log(e, e.detail);
      }

      // invalid tag added callback
      function onInvalidTag(e){
        console.log(e, e.detail);
      }
      console.log(  tagify.value )
    });

  });
  $(document).on('change', '.filter_list', function(){
    var button_id = $(this).attr("id");
    var value = $('#filter_option'+button_id+'').val();
    // alert(button_id+"    |    "+value + "       |      "+i);
    if(value == "1"){
      $('#position_value'+button_id+'').show();
    } else {
      $('#position_value'+button_id+'').hide();
    }
    if(value == "2"){
      $('#salary_value'+button_id+'').show();
    } else {
      $('#salary_value'+button_id+'').hide();
    }
    if(value == "3"){
      $('#age_value'+button_id+'').show();
    } else {
      $('#age_value'+button_id+'').hide();
    }
    if(value == "4"){
      $('#gender_value'+button_id+'').show();
    } else {
      $('#gender_value'+button_id+'').hide();
    }
    if(value == "5"){
      $('#nationality_value'+button_id+'').show();
    } else {
      $('#nationality_value'+button_id+'').hide();
    }
    if(value == "6"){
      $('#status_value'+button_id+'').show();
    } else {
      $('#status_value'+button_id+'').hide();
    }
    if(value == "7"){
      $('#edu_value'+button_id+'').show();
    } else {
      $('#edu_value'+button_id+'').hide();
    }
    if(value == "8"){
      $('#university_value'+button_id+'').show();
    } else {
      $('#university_value'+button_id+'').hide();
    }
    if(value == "9"){
      $('#faculty_value'+button_id+'').show();
    } else {
      $('#faculty_value'+button_id+'').hide();
    }
    if(value == "11"){
      $('#gpa_value'+button_id+'').show();
    } else {
      $('#gpa_value'+button_id+'').hide();
    }
    if(value == "12"){
      $('#comskill_value'+button_id+'').show();
    } else {
      $('#comskill_value'+button_id+'').hide();
    }
    if(value == "10"){
      $('#major_value'+button_id+'').show();
    } else {
      $('#major_value'+button_id+'').hide();
    }
    if(value == "13"){
      $('#language_value'+button_id+'').show();
    } else {
      $('#language_value'+button_id+'').hide();
    }
    if(value == "14"){
      $('#experience_value'+button_id+'').show();
    } else {
      $('#experience_value'+button_id+'').hide();
    }
    if(value == "15"){
      $('#workexp_value'+button_id+'').show();
    } else {
      $('#workexp_value'+button_id+'').hide();
    }

  });

  // Legacy REMOVE
  // $(document).on('click', '.btn_remove', function(){
  //   // alert("เข้าเว้ยยย" + i)
  //   var button_id = $(this).attr("id");
  //   $('#'+button_id+'').remove();
  //   // i=i-1;
  // });

  // Remove w/ Jquery Style
  $(document).on('click', '.btn_remove', function(){
    var button_id = $(this).attr("id");
    $.confirm({
      title: 'Delete this Filter Criteria ?!',
      content: "คุณต้องการลบคุณสมบัติในการคัดกรองผู้สมัครนี้หรือไม่?",
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
