import React from 'react'
import '../estilo/style.css'
import PruebaItem from './PruebaItem'
import { Link } from 'react-router-dom'
class Prueba extends React.Component{
    constructor(){
        super();
        this.state = {
            titulo: "Cuestionario sobre la salud del paciente -9 (PHQ-9)",
            cuestio: [{
                id: 1,
                pregunta: "Poco interés o placer en hacer las cosas",
                valor: 0
            },
            {
                id: 2,
                valor: 0,
                pregunta: "Sentirse desanimado/a, deprimido/a o sin esperanzas"
            },
            {
                id: 3,
                valor: 0,
                pregunta: "Dificultades para quedarse dormido/a o mantenerse durmiendo, o dormir demasiado"
            },
            {
                id: 4,
                valor: 0,
                pregunta: "Sentirse cansado/a o con poca energía"
            },
            {
                id: 5,
                valor: 0,
                pregunta: "Poco apetito o comer en exceso"
            },
            {
                id: 6,
                valor: 0,
                pregunta: "Sentirse mal acerca de sí mismo/a — o sentir que es un/afracasado/a o que se ha fallado a sí mismo/a o a su familia"
            },
            {
                id: 7,
                valor: 0,
                pregunta: "Dificultad para concentrarse en las cosas, tales como leer el diario o ver televisión"
            },
            {
                id: 8,
                valor: 0,
                pregunta: "¿Moverse o hablar tan despacio que otras personas lo pueden haber notado? O lo contrario — estar tan inquieto/a o intranquilo/a que se ha estado moviendo mucho más de lo normal"
            },
            {
                id: 9,
                valor: 0,
                pregunta: "Pensamientos de que sería mejor estar muerto/a o que quisiera lastimarse a si mismo/a de alguna forma"
            }
            ],
            cuestio2: [{
                id: 1,
                valor: 0,
                pregunta: "Sentirse nervioso/a, intranquilo/a o con los nervios de punta"
            },
            {
                id: 2,
                valor: 0,
                pregunta: "No poder dejar de preocuparse o no poder controlar la preocupación"
            },
            {
                id: 3,
                valor: 0,
                pregunta: "Preocuparse demasiado por diferentes cosas"
            },
            {
                id: 4,
                valor: 0,
                pregunta: "Dificultad para relajarse"
            },
            {
                id: 5,
                valor: 0,
                pregunta: "Estar tan inquieto/a que es difícil permanecer sentado/a tranquilamente"
            },
            {
                id: 6,
                valor: 0,
                pregunta: "Molestarse o ponerse irritable fácilmente"
            },
            {
                id: 7,
                valor: 0,
                pregunta: "Sentir miedo como si algo terrible pudiera pasar"
            }],
            prueba: 1,
            puntos: 0

        }
        this.totalPoints = this.totalPoints.bind(this);
    }
    switchPrueba(num){
        if(num != this.state.prueba){
            this.setState({prueba: num})
            var radios = document.getElementsByTagName("input");
            var i;
            for(i=0; i<radios.length; i++){
                radios[i].checked = false;
            }
            if(num == 1){
                this.setState({titulo: "Cuestionario sobre la salud del paciente -9 (PHQ-9)"})
            }
            else{
                this.setState({titulo: "GAD-7"})
            }
            var bttn = document.getElementById('bt1');
            var bttn2 = document.getElementById('bt2');
            bttn.classList.toggle('sele');
            bttn2.classList.toggle('sele');
        }
        
    }

    totalPoints(num, previous, ids){
        this.setState({puntos: this.state.puntos - previous + num})
        if(this.state.prueba == 1){
            let cuestioa = [...this.state.cuestio];
            let item = {...cuestioa[ids-1]};
            item.valor = num;
            cuestioa[ids-1] = item;
            this.setState({cuestio: cuestioa})
        }
        else{
            let cuestio2 = [...this.state.cuestio2];
            let item = {...cuestio2[ids-1]};
            item.valor = num;
            cuestio2[ids-1] = item;
            this.setState({cuestio2: cuestio2})
        }
        
    }
    render(){
        var questionsList = <div></div>
        if(this.state.prueba == 1){
            questionsList = this.state.cuestio.map(item => <PruebaItem key={item.id} item={item} pregunta={this.state.pregunta} totalPoints={this.totalPoints} />)
        }
        else{
            questionsList = this.state.cuestio2.map(item => <PruebaItem key={item.id} item={item} pregunta={this.state.pregunta} totalPoints={this.totalPoints} />)
        }

        return(
            <div className="Gridm">
                <div style={{width: '95%', marginRight: 'auto', marginLeft: '5%', marginTop: '1%'}}>
                    <h1 className="titulo"> {this.state.titulo}</h1>
                    <h2 className="tituloc"> Durante las dos últimas semanas, ¿con qué frecuencia
                        ha sentido molestias debido a cualquiera de los
                        siguientes problemas?  
                    </h2>
                    <h2 className="tituloc">
                        (Marque con un “✔” para indicar su respuesta)
                    </h2>
                    <br></br>
                        {questionsList}
                        <h1 className="conten" style={{textAlign: 'center', marginBottom: '2%'}}>
                            {'Puntaje Final: ' + this.state.puntos}
                        </h1>
                </div>  
                <div>
                    <button id='bt1' onClick={() => {this.switchPrueba(1)}} className="btt" style={{width: '90%', height: '5%'}}>PRUEBA DE DEPRESION</button> 
                    <button id='bt2' onClick={() => {this.switchPrueba(2)}} className="btt sele" style={{width: '90%', height: '5%'}}>PRUEBA DE ANSIEDAD</button> 
                </div>
            </div>
        )
    }
}
export default Prueba