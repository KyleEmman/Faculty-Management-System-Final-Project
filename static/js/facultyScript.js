
function logout(url) {
    Swal.fire({
        title: 'Are you sure that you want to logout?',
        showCancelButton: true,
        confirmButtonText: "Confirm",
        confirmButtonColor: "#FF6961"
    }).then((result) => {
        if (result.isConfirmed) {
            return location.href = url
        }
        else if (result.isDenied) {
            return false
        }
    })
}
