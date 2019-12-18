

var contenido = document.querySelector('#contenido')
function traer() {
    fetch('https://mindicador.cl/api')
        .then(res => res.json())
        .then(datos => {
            /* console.log(datos)  */
            /* console.log(datos[0]); */
            /* contenido.innerHTML = `${datos.utm.unidad_medida}`; */
            for (let key in datos) {
                /* console.log(datos[key].codigo) */
                if (datos[key].codigo != undefined) 

                /* if (datos[key].codigo == "dolar" || datos[key].codigo == "euro") */
                {
                    var fecha = new Date (datos[key].fecha)
                    var hora = new Date(fecha.toLocaleTimeString())
                    /* var hora = new Time (datos[key].fecha)
                    console.log(hora) */
                    console.log(datos[key].fecha)

                    contenido.innerHTML += ` 
                                   
                    <tr>
                        <td>${ datos[key].codigo}</td>
                        <td>${ datos[key].nombre}</td>
                        <td>${ datos[key].unidad_medida}</td>
                        <td>${fecha.toLocaleDateString() + " "+ fecha.toLocaleTimeString()} </td>
                        
                        <td>${ datos[key].valor.toFixed(2)} </td>
                    </tr>                
                    `
                }
               
            }
        })
}