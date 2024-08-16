function save() {
    // Obtener los valores del formulario
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const birthdate = document.getElementById('birthdate').value;
    const gender = document.getElementById('gender').value;

    // Validar campos vacíos
    if (!name || !phone || !birthdate || !gender) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    // Validar fecha de nacimiento (debe ser menor a la fecha actual)
    const today = new Date();
    const birthDate = new Date(birthdate);

    if (birthDate >= today) {
        alert("La fecha de nacimiento debe ser menor a la fecha actual.");
        return;
    }

    const formData = {
        name: name,
        phone: phone,
        birthdate: birthdate,
        gender: gender
    };

    fetch('/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        // Limpiar los campos del formulario
        document.getElementById('name').value = '';
        document.getElementById('phone').value = '';
        document.getElementById('birthdate').value = '';
        document.getElementById('gender').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });

}