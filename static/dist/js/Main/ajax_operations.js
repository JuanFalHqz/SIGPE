function eliminarObject(id, _url, name) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    });

    $("#name_object").html(name);
    document.getElementById('delete_obj').onclick = function () {
        $.ajax({
            url: _url,
            type: 'get',
            data: {
                'pk': id
            },
            dataType: 'json',
            success: (data) => {
                if (data.deleted) {
                    $("#modal-delete").modal('hide');
                    $("#example1 tbody #row-" + id).remove();
                    Toast.fire({
                        icon: 'success',
                        title: 'Proyecto ' + name + ' eliminado correctamente.'
                    })
                } else {
                    Swal.fire({
                        title: 'Ha ocurrido un error.',
                        text: data.errors,
                        icon: 'error'
                    });
                }
            },
        })
    };
}
//all-elements
//btn-all-delete