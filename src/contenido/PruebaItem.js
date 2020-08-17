import React from 'react'
import '../estilo/style.css'
import '../estilo/prueba.css'

function ProjectItem(props){
    return(
        <div className="Gridc">
            <p className="conten">
                {props.item.pregunta}
            </p>
            <div>
            <ul>
                    <li><input id={"0" + props.item.id} type="radio" name={'p' + props.item.id}/>
                    <label for={"0" + props.item.id}>0</label>
                    <div className="check"></div></li>
                    <li><input id={"1" + props.item.id} type="radio" name={'p' + props.item.id}/>
                    <label for={"1" + props.item.id}>1</label>
                    <div className="check"></div></li>
                    <li><input id={"2" + props.item.id} type="radio" name={'p' + props.item.id}/>
                    <label for={"2" + props.item.id}>2</label>
                    <div className="check"></div></li>
                    <li><input id={"3" + props.item.id} type="radio" name={'p' + props.item.id}/>
                    <label for={"3" + props.item.id}>3</label>
                    <div className="check"></div></li>

                </ul>
            </div>
        </div>
    )
}
export default ProjectItem;