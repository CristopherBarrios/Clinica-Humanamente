import React from 'react'
import '../estilo/style.css'
import '../estilo/prueba.css'

function ContactoItem(props){
    let descrip = props.item.desc.split('\n').map((item, i) => {
        return <p key={i}>{item}</p>;
    })
    var divider = <p />
    if (props.item.id == 6){
        divider = <p>Asociados</p>
    }
    return(
        <div>
            <div className="GridCon">
                <img className='Perfil' src={props.item.foto} />

                <div>
                    <div style={{ fontSize: '25px', color:'#016495'}}>
                        <p className='quienp'>{props.item.nombre}</p></div>

                    <div className='quiend' style={{fontSize: '20px', textAlign: 'justify'}}>
                        {descrip}
                    </div>
                </div>
            </div>
            <div className='quient' style={{ marginTop: '3%', textAlign: "center", fontSize: '33px', color:'#016495'}}>{divider}</div>
        </div>
    )
}
export default ContactoItem;