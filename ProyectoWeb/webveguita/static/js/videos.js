function openModal(videoUrl) {
    var modal = document.getElementById("myModal");
    var videoFrame = document.getElementById("videoFrame");
    videoFrame.src = videoUrl;
    modal.style.display = "block";
}

function closeModal() {
    var modal = document.getElementById("myModal");
    var videoFrame = document.getElementById("videoFrame");
    videoFrame.src = "";
    modal.style.display = "none";
}