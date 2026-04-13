//----------------------------------------------------------------
// siri harshitha code start here 
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
    
    // --- ADDED: ESC Key to Exit Chatbot ---
    $(document).keydown(function (e) {
        if (e.keyCode === 27) { // 27 is the ESC key
            console.log("ESC pressed: Stopping chatbot session...");
            
            // Trigger Python to stop speech/logic
            eel.stop_chatbot_session()();

            // UI Reset
            $("#SiriWave").attr("hidden", true);
            $("#Oval").attr("hidden", false);
            
            // Clear chatbox
            $("#chatbox").val("");
        }
    });
    // --------------------------------------
    // Expose this function so Python can call it
eel.expose(triggerSiriWave);
function triggerSiriWave() {
    console.log("Hotword Signal Received from Python!");
    
    // Play the 'listening' sound
    eel.playAssistantSound()();

    // VISUAL SWITCH
    $("#Oval").attr("hidden", true);      // Hide the static circle
    $("#SiriWave").attr("hidden", false); // Show the Siri wave
    
    // This ensures the wave starts moving if it was paused
    if (siriWave) { siriWave.start(); }
    // Start the voice command listener
    eel.allCommands()(); 
}

    // 5. Load Settings Data from Python
    eel.personalInfo()();
    eel.displaySysCommand()();
    eel.displayWebCommand()();
    eel.displayPhoneBookCommand()();
// siri harshitha code end here 

    //execute: python side: 
    // rachan code start form here 
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


// rachana code end here 