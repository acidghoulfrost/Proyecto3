function validarOpinion() {
    var opinion = document.getElementById("areatexto").value.trim();
    
    if (opinion === "") {
        alert("Por favor, ingresa tu opinión antes de enviar.");
        return false;
    }
    
    return true;
}

function validarYLimpiarFormulario() {
    var nombre = document.getElementById('nombre').value.trim();
    var apellido = document.getElementById('apellido').value.trim();
    var tipopaquete = document.getElementById('tipopaquete').value;
    var message = document.getElementById('areadetalle').value.trim();

    if (nombre === '' || apellido === '' || tipopaquete === '' || message === '') {
        alert('Por favor completa todos los campos.');
        return false;
    }

    document.getElementById('nombre').value = '';
    document.getElementById('apellido').value = '';
    document.getElementById('tipopaquete').value = 'Caja pequeña';
    document.getElementById('areadetalle').value = '';

    return true;
}
