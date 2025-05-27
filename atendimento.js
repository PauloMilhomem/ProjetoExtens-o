function openPopup(type) {
      document.getElementById('overlay').classList.add('active');
      document.getElementById('popup-' + type).classList.add('active');
    }

    function closePopup() {
      document.getElementById('overlay').classList.remove('active');
      document.querySelectorAll('.popup').forEach(popup => popup.classList.remove('active'));
    }