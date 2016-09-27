var _validAudioFileExtensions = [".mp3"];
var _validImageFileExtensions = [".jpg", ".jpeg", ".png"];
function ValidateAudioSingleInput(oInput) {
    if (oInput.type == "file") {
        var sFileName = oInput.value;
         if (sFileName.length > 0) {
            var blnValid = false;
            for (var j = 0; j < _validAudioFileExtensions.length; j++) {
                var sCurExtension = _validAudioFileExtensions[j];
                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                    blnValid = true;
                    break;
                }
            }

            if (!blnValid) {
                
                runPopup("Sorry, " + sFileName + " is invalid, allowed extensions are: " + _validAudioFileExtensions.join(", "));
                oInput.value = "";
                return false;
            }
        }
    }
    return true;
}

function ValidateImageSingleInput(oInput) {
    if (oInput.type == "file") {
        var sFileName = oInput.value;
         if (sFileName.length > 0) {
            var blnValid = false;
            for (var j = 0; j < _validImageFileExtensions.length; j++) {
                var sCurExtension = _validImageFileExtensions[j];
                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                    blnValid = true;
                    break;
                }
            }

            if (!blnValid) {
                runPopup("Sorry, " + sFileName + " is invalid, allowed extensions are: " + _validImageFileExtensions.join(", "));
                oInput.value = "";
                return false;
            }
        }
    }
    return true;
}

document.addEventListener('DOMContentLoaded', ready);

function ready(){
    document.addEventListener('click', function(event){
        if(event.target.classList.contains('close-popup')){
            closePopup(event.target);
        }
    });
    jQuery( 'audio' ).audioPlayer();
}

function closePopup(el){
    var parent = el;
    while(parent.getAttribute('id') != 'popup'){
        parent = parent.parentNode;
    }
    parent.classList.add('hide');
    parent.querySelector('.popup').classList.remove('fade');
}

function runPopup(msg){
    var popup = document.getElementById('popup');
    popup.querySelector('.popup-msg').innerText = msg;
    popup.classList.remove('hide');
    popup.querySelector('.popup').classList.add('fade-in');
}