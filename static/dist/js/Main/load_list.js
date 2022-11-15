$(document).ready(() => {
    //Variable imprescindible para los mensajes de alerta satisfactorios
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
    //identificadores de los elementos
    /*
    * Para que funcione correctamente debes poner en la cabecera de ta tabla un checkbox con id='all-elements'
    * y luego a cada checkbox del body de la tabla la clase class='checkbox'.
    * En ids se almacenan los id a eliminar
    * */
    ids = [];
    // Selecciona y deselecciona todos los chequed
    $("#all-elements").click(() => {
        if ($("#all-elements").prop('checked')) {
            $('.checkbox').each(function (i) {
                $(this).prop('checked', true);
                ids[i] = $(this).val();
            });
        } else {
            $('.checkbox').each(function (i) {
                $(this).prop('checked', false);
                ids = [];
            });
        }
    });

    $("#btn-all-delete").click((e) => {
        ids = [];
        //guardo los id de los checkbox seleccionados.
        $('.checkbox:checked').each(function (i) {
            console.log($(this).val())
            ids[i] = $(this).val();
        })
        if (ids.length == 0) {
            Swal.fire({
                title: 'Ha ocurrido un error.',
                text: "Seleccione los elementos a borrar.",
                icon: 'warning'
            });
        } else {
            let url = $("#btn-all-delete").val();
            console.log('Url');
            $.ajax({
                url: url,
                type: 'get',
                data: {'list_id[]': ids},
                dataType:'json',
                success:(data)=>{
                    if (data.deleted) {
                        $("#modal-delete").modal('hide');
                        ids.forEach((value)=>{
                            console.log('value:'+value)
                            $("#example1 tbody #row-" + value).remove();
                        })
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
                    Toast.fire({
                        icon: 'success',
                        title: 'Se han eliminado' +ids.length+ ' elementos correctamente.',
                    })
                }
            })
        }
        console.log(ids);
    })
})