import {useEffect, useState} from "react";
import {getAirplanes} from "../../services/API";
import Airplane from "../Airplane/Airplane";
import AirplaneInfo from "../AirplaneInfo/AirplaneInfo";
import Form from "../Form/Form";

export default function Airplanes() {
    const [airplanes, setAirplanes] = useState()
    const [idOfChosen, setIdOfChosen] = useState()
    useEffect(() => {
        getAirplanes().then(value => {
            setAirplanes([...value.data])
        })
    }, [])

    function aboutAirplane(id) {
        setIdOfChosen(id)
    }
    return (
        <div>
            {airplanes && airplanes.map(value => <Airplane item={value} key={value.id} aboutAirplane={aboutAirplane}/>)}
            {idOfChosen && <AirplaneInfo id={idOfChosen}/>}
            <h2>CREATE NEW AIRPLANE</h2>
            <Form do_you_wont_update_component={false} item={''}/>
        </div>
    );
}