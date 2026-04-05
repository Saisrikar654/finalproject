// $(document).ready(function () {

//   eel.init()()
//   // Title Animation
//   // $('.text').textillate({
//   //   loop: true,
//   //   sync: true,
//   //   in: { effect: "fadeIn" },
//   //   out: { effect: "fadeOut" }
//   // });


//   $('.title-text').textillate({
//     loop: true,
//     sync: true,
//     in: { effect: "fadeIn" },
//     out: { effect: "fadeOut" }
//   });

//   // Subtitle Animation - for Ask me anything...
//   $('.text').textillate({
//     loop: true,
//     sync: true,
//     in: { effect: "fadeOut" },
//     out: { effect: "fadeIn" }
//   });

//   // SiriWave Setup
//   var siriWave = new SiriWave({
//     container: document.getElementById("siri-container"),
//     width: 800,
//     height: 200,
//     style: "ios9",
//     amplitude: "1",
//     speed: "0.2",
//     autostart: true
//   });

//   // Paragraph Animation — only once
//   $('.siri-message').textillate({
//     loop: true,
//     sync: true,
//     in: {
//       effect: "fadeInUp",
//       sync: true,
//     },
//     out: {
//       effect: "fadeOutUp",
//       sync: true,

//     }
//   });

//   // mic button

//   $("#MicBtn").click(function () {
//     eel.playAssistantSound()
//     $("#Oval").attr("hidden", true);
//     $("#SiriWave").attr("hidden", false);
//     eel.allCommands()()
//   });

//   function doc_keyUp(e) {

//     if (e.key === 'o' && e.metaKey) {
//       eel.playAssistantSound()
//       $("#Oval").attr("hidden", true);
//       $("#SiriWave").attr("hidden", false);
//       eel.allCommands()()
//     }
//   }
//   document.addEventListener('keyup', doc_keyUp, false);

//   function PlayAssistant(message) {

//     if (message != "") {

//       $("#Oval").attr("hidden", true);
//       $("#SiriWave").attr("hidden", false);
//       eel.allCommands(message);
//       $("#chatbox").val("")
//       $("#MicBtn").attr('hidden', false);
//       $("#SendBtn").attr('hidden', true);

//     }

//   }
//   function ShowHideButton(message) {
//     if (message.length == 0) {
//       $("#MicBtn").attr('hidden', false);
//       $("#SendBtn").attr('hidden', true);
//     }
//     else {
//       $("#MicBtn").attr('hidden', true);
//       $("#SendBtn").attr('hidden', false);
//     }
//   }

//   $("#chatbox").keyup(function () {

//     let message = $("#chatbox").val();
//     ShowHideButton(message)

//   });

//   // send button event handler
//   $("#SendBtn").click(function () {

//     let message = $("#chatbox").val()
//     PlayAssistant(message)

//   });

//   // enter press event handler on chat box
//   $("#chatbox").keypress(function (e) {
//     key = e.which;
//     if (key == 13) {
//       let message = $("#chatbox").val()
//       PlayAssistant(message)
//     }
//   });

//   // $("#MicBtn").click(function () {
//   //   // const selectedLang = $("#languageSelector").val(); // Get selected language

//   //   eel.playAssistantSound(); // Optional: if you play a mic sound
//   //   $("#Oval").attr("hidden", true);
//   //   $("#SiriWave").attr("hidden", false);

//   //   // Call Python's takecommand with selected language
//   //   eel.takecommand(selectedLang)(function (result) {
//   //     console.log("User said:", result);
//   // Optional: speak the result or display it
//   // eel.DisplayMessage(result);
//   // eel.ShowHood(); 

// });

// // Settings Code

// eel.personalInfo()();
// eel.displaySysCommand()();
// eel.displayWebCommand()();
// eel.displayPhoneBookCommand()();



// // Execute: python side :
// eel.expose(getData)
// function getData(user_info) {
//   let data = JSON.parse(user_info);
//   let idsPersonalInfo = ['OwnerName', 'Designation', 'MobileNo', 'Email', 'City']
//   let idsInputInfo = ['InputOwnerName', 'InputDesignation', 'InputMobileNo', 'InputEmail', 'InputCity']

//   for (let i = 0; i < data.length; i++) {
//     hashid = "#" + idsPersonalInfo[i]
//     $(hashid).text(data[i]);
//     $("#" + idsInputInfo[i]).val(data[i]);
//   }

// }

// // Personal Data Update Button:

// $("#UpdateBtn").click(function () {

//   let OwnerName = $("#InputOwnerName").val();
//   let Designation = $("#InputDesignation").val();
//   let MobileNo = $("#InputMobileNo").val();
//   let Email = $("#InputEmail").val();
//   let City = $("#InputCity").val();

//   if (OwnerName.length > 0 && Designation.length > 0 && MobileNo.length > 0 && Email.length > 0 && City.length > 0) {
//     eel.updatePersonalInfo(OwnerName, Designation, MobileNo, Email, City)

//     swal({
//       title: "Updated Successfully",
//       icon: "success",
//     });


//   }
//   else {
//     const toastLiveExample = document.getElementById('liveToast')
//     const toast = new bootstrap.Toast(toastLiveExample)

//     $("#ToastMessage").text("All Fields Medatory");

//     toast.show()
//   }

// });
// // Display System Command Method
// eel.expose(displaySysCommand)
// function displaySysCommand(array) {

//   let data = JSON.parse(array);
//   console.log(data)

//   let placeholder = document.querySelector("#TableData");
//   let out = "";
//   let index = 0
//   for (let i = 0; i < data.length; i++) {
//     index++
//     out += `
//                     <tr>
//                         <td class="text-light"> ${index} </td>
//                         <td class="text-light"> ${data[i][1]} </td>
//                         <td class="text-light"> ${data[i][2]} </td>
//                         <td class="text-light"> <button id="${data[i][0]}" onClick="SysDeleteID(this.id)" class="btn btn-sm btn-glow-red">Delete</button></td>
                        
//                     </tr>
//             `;

//     // console.log(data[i][0])
//     // console.log(data[i][1])


//   }

//   placeholder.innerHTML = out;

// }

// // Add System Command Button
// $("#SysCommandAddBtn").click(function () {

//   let key = $("#SysCommandKey").val();
//   let value = $("#SysCommandValue").val();

//   if (key.length > 0 && value.length) {
//     eel.addSysCommand(key, value)

//     swal({
//       title: "Updated Successfully",
//       icon: "success",
//     });
//     eel.displaySysCommand()();
//     $("#SysCommandKey").val("");
//     $("#SysCommandValue").val("");


//   }
//   else {
//     const toastLiveExample = document.getElementById('liveToast')
//     const toast = new bootstrap.Toast(toastLiveExample)

//     $("#ToastMessage").text("All Fields Medatory");

//     toast.show()
//   }

// });

// // Display Web Commands Table
// eel.expose(displayWebCommand)
// function displayWebCommand(array) {

//   let data = JSON.parse(array);
//   console.log(data)

//   let placeholder = document.querySelector("#WebTableData");
//   let out = "";
//   let index = 0
//   for (let i = 0; i < data.length; i++) {
//     index++
//     out += `
//                     <tr>
//                         <td class="text-light"> ${index} </td>
//                         <td class="text-light"> ${data[i][1]} </td>
//                         <td class="text-light"> ${data[i][2]} </td>
//                         <td class="text-light"> <button id="${data[i][0]}" onClick="WebDeleteID(this.id)" class="btn btn-sm btn-glow-red">Delete</button></td>
                        
//                     </tr>
//             `;

//     // console.log(data[i][0])
//     // console.log(data[i][1])


//   }

//   placeholder.innerHTML = out;

// }


// // Add Web Commands

// $("#WebCommandAddBtn").click(function () {

//   let key = $("#WebCommandKey").val();
//   let value = $("#WebCommandValue").val();

//   if (key.length > 0 && value.length) {
//     eel.addWebCommand(key, value)

//     swal({
//       title: "Updated Successfully",
//       icon: "success",
//     });
//     eel.displayWebCommand()();
//     $("#WebCommandKey").val("");
//     $("#WebCommandValue").val("");


//   }
//   else {
//     const toastLiveExample = document.getElementById('liveToast')
//     const toast = new bootstrap.Toast(toastLiveExample)

//     $("#ToastMessage").text("All Fields Medatory");

//     toast.show()
//   }

// });

// // Display Phone Book

// eel.expose(displayPhoneBookCommand)
// function displayPhoneBookCommand(array) {

//   let data = JSON.parse(array);
//   console.log(data)

//   let placeholder = document.querySelector("#ContactTableData");
//   let out = "";
//   let index = 0
//   for (let i = 0; i < data.length; i++) {
//     index++
//     out += `
//               <tr>
//                   <td class="text-light"> ${index} </td>
//                   <td class="text-light"> ${index} </td>
//                   <td class="text-light"> ${data[i][1]} </td>
//                   <td class="text-light"> ${data[i][2]} </td>
//                   <td class="text-light"> ${data[i][3]} </td>
//                   <td class="text-light"> ${data[i][4]} </td>
//                   <td class="text-light"> <button id="${data[i][0]}" onClick="ContactDeleteID(this.id)" class="btn btn-sm btn-glow-red">Delete</button></td>
                        
//               </tr>
//             `;


//   }

//   placeholder.innerHTML = out;

// }

// // Add Contacts to database

// $("#AddContactBtn").click(function () {

//   let Name = $("#InputContactName").val();
//   let MobileNo = $("#InputContactMobileNo").val();
//   let Email = $("#InputContactEmail").val();
//   let City = $("#InputContactCity").val();

//   if (Name.length > 0 && MobileNo.length > 0) {

//     if (Email.length < 0) {
//       Email = "";
//     }
//     else if (City < 0) {
//       City = "";
//     }

//     eel.InsertContacts(Name, MobileNo, Email, City)

//     swal({
//       title: "Updated Successfully",
//       icon: "success",
//     });

//     $("#InputContactName").val("");
//     $("#InputContactMobileNo").val("");
//     $("#InputContactEmail").val("");
//     $("#InputContactCity").val("");
//     eel.displayPhoneBookCommand()()

//   }
//   else {
//     const toastLiveExample = document.getElementById('liveToast')
//     const toast = new bootstrap.Toast(toastLiveExample)

//     $("#ToastMessage").text("Name and Mobile number Madatory");

//     toast.show()
//   }
// });

// // }); NEED TO CHECK THIS
// function SysDeleteID(clicked_id) {


//     // console.log(clicked_id);
//     eel.deleteSysCommand(clicked_id)
//     eel.displaySysCommand()();

// }

// function WebDeleteID(clicked_id) {


//     // console.log(clicked_id);
//     eel.deleteWebCommand(clicked_id)
//     eel.displayWebCommand()();


// }
// function ContactDeleteID(clicked_id) {

//     // console.log(clicked_id);
//     eel.deletePhoneBookCommand(clicked_id)
//     eel.displayPhoneBookCommand()();

// }
$(document).ready(function () {

    // 1. Initialize Eel
    eel.init()();

    // 2. Animation Setups
    $('.title-text').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeIn" },
        out: { effect: "fadeOut" }
    });

    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeOut" },
        out: { effect: "fadeIn" }
    });

    // 3. SiriWave Setup
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.2",
        autostart: true
    });

    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeInUp", sync: true },
        out: { effect: "fadeOutUp", sync: true }
    });

    // 4. Input & Mic Handlers
    $("#MicBtn").click(function () {
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()();
    });

    function PlayAssistant(message) {
        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("");
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
    }

    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        } else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    $("#chatbox").keyup(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });

    $("#SendBtn").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

    $("#chatbox").keypress(function (e) {
        if (e.which == 13) {
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });

    // 5. Load Settings Data from Python
    eel.personalInfo()();
    eel.displaySysCommand()();
    eel.displayWebCommand()();
    eel.displayPhoneBookCommand()();


    //execute: python side: 
  eel.expose(getData)
  function getData(user_info) {
    let data = JSON.parse(user_info);
    let idsPersonalInfo = ['OwnerName', 'Designation', 'MobileNo', 'Email', 'City'];
    let idsInputInfo = ['InputOwnerName', 'InputDesignation', 'InputMobileNo', 'InputEmail', 'InputCity'];

    for (let i = 0; i < data.length; i++) {
        hashid = "#" + idsPersonalInfo[i]
        $(hashid).text(data[i]);
        $("#" + idsPersonalInfo[i]).val(data[i]);
    }
} 

    // 6. Update Personal Info Button
    $("#UpdateBtn").click(function () {
        let OwnerName = $("#InputOwnerName").val();
        let Designation = $("#InputDesignation").val();
        let MobileNo = $("#InputMobileNo").val();
        let Email = $("#InputEmail").val();
        let City = $("#InputCity").val();

        if (OwnerName.length > 0 && Designation.length > 0 && MobileNo.length > 0 && Email.length > 0 && City.length > 0) {
            eel.updatePersonalInfo(OwnerName, Designation, MobileNo, Email, City)

            swal({ 
                title: "Updated Successfully", 
                icon: "success" 
            });

        } 
        else {
            const toastLiveExample = document.getElementById('liveToast');
            const toast = new bootstrap.Toast(toastLiveExample);
            $("#ToastMessage").text("All Fields Mandatory");
            toast.show()
        }
    });

    // Display system command method
   eel.expose(displaySysCommand)
   function displaySysCommand(array) {
    let data = JSON.parse(array);
    console.log(data)

    let placeholder = document.querySelector("#TableData");
    let out = "";
    let index = 0
    for(let i = 0; i < data.length; i++) {
        out += `
                <tr>
                    <td class="text-light">${index + 1}</td>
                    <td class="text-light">${data[1]}</td>
                    <td class="text-light">${data[2]}</td>
                    <td class="text-light"><button id="${data[0]}" onClick="SysDeleteID(this.id)" class="btn btn-sm btn-glow-red">Delete</button></td>
                </tr>
        `;

    }

    placeholder.innerHTML = out;
        
}

    // 7. Add Command Buttons
    $("#SysCommandAddBtn").click(function () {
        let key = $("#SysCommandKey").val();
        let value = $("#SysCommandValue").val();
        if (key.length > 0 && value.length > 0) {
            eel.addSysCommand(key, value);
            swal({
                 title: "Updated Successfully",
                  icon: "success" });
            eel.displaySysCommand()();
            $("#SysCommandKey").val("");
            $("#SysCommandValue").val("");
        }
        else{
            const toastLiveExample = document.getElementById('liveToast')
            const toast = new bootstrap.Toast(toastLiveExample)

            $("ToastMessage").text("All Fields Medatory");
            toast.show()
        }
    });
// Display web commands table 
eel.expose(displayWebCommand);
function displayWebCommand(array) {
    let data = JSON.parse(array);
    console.log(data)

    let placeholder = document.querySelector("#WebTableData");
    let out = "";
    let index = 0;
    for(let i = 0; i < data.length; i++) {
        index++
        out += `
            <tr>
                <td class="text-light">${index + 1}</td>
                <td class="text-light">${data[i][1]}</td>
                <td class="text-light">${data[i][2]}</td>
                <td class="text-light"><button id="${data[i][0]}" onClick="WebDeleteID(this.id)" class="btn btn-sm btn-glow-red">Delete</button></td>
            </tr>
        `;
    }
    placeholder.innerHTML = out;
}

    $("#WebCommandAddBtn").click(function () {

        let key = $("#WebCommandKey").val();
        let value = $("#WebCommandValue").val();

        if (key.length > 0 && value.length > 0) {
            eel.addWebCommand(key, value);

            swal({ 
                title: "Updated Successfully", 
                icon: "success"
             });
            eel.displayWebCommand()();
            $("#WebCommandKey").val("");
            $("#WebCommandValue").val("");
        }
        else{
            const toastLiveExample = document.getElementById('liveToast')
            const toast= new bootstrap.Toast(toastLiveExample)

            $("ToastMessage").text("All Fields Medatory");
            toast.show()
        }
    });

    // Display phone book commands table

    eel.expose(displayPhoneBookCommand);
    function displayPhoneBookCommand(array) {
        let data = JSON.parse(array);
        console.log(data)

        let placeholder = document.querySelector("#ContactTableData");
        let out = "";
        let index = 0;
        for(let i = 0; i< data.length; i++) {
            index++
            out += `
                    <tr>
                        <td class="text-light">${index}</td>
                        <td class="text-light">${data[i][1]}</td>
                        <td class="text-light">${data[i][2]}</td>
                        <td class="text-light">${data[i][3]}</td>
                        <td class="text-light">${data[i][4]}</td>
                        <td class="text-light"><button id="${data[i][0]}" onClick="ContactDeleteID(this.id)" class="btn btn-sm btn-glow-red">Delete</button></td>
                    </tr>
            `;
    }
    placeholder.innerHTML = out;
}



    $("#AddContactBtn").click(function () {
        let Name = $("#InputContactName").val();
        let MobileNo = $("#InputContactMobileNo").val();
        let Email = $("#InputContactEmail").val();
        let City = $("#InputContactCity").val();

        if (Name.length > 0 && MobileNo.length > 0) {

            if(Email.length <0) {
                Email = "";
            }
            else if (City < 0) {
                City = "";
            }
            eel.InsertContacts(Name, MobileNo, Email, City);

            swal({ 
                title: "Updated Successfully", 
                icon: "success" 
            });
            $("#InputContactName").val("");
            $("#InputContactMobileNo").val("");
            $("#InputContactEmail").val("");
            $("#InputContactCity").val("");
            eel.displayPhoneBookCommand()();
        }
        else{
            const toastLiveExample = document.getElementById('liveToast')
            const toast = new bootstrap.Toast(toastLiveExample)

            $("#ToastMessage").text("Name and Moblie number Madatory");
            
            toast.show()
        }
    });

}); // End of Document Ready

function SysDeleteID(clicked_id) {

    eel.deleteSysCommand(clicked_id);
    eel.displaySysCommand()();
}

function WebDeleteID(clicked_id) {
    eel.deleteWebCommand(clicked_id);
    eel.displayWebCommand()();
}

function ContactDeleteID(clicked_id) {
    eel.deletePhoneBookCommand(clicked_id);
    eel.displayPhoneBookCommand()();
}
