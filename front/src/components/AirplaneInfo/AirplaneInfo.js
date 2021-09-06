import {useEffect, useState} from "react";
import {deleteAirplane, getAirplane} from "../../services/API";
import Form from "../Form/Form";

export default function AirplaneInfo({id}) {
    const [chosen, setChosen] = useState()
    useEffect(() => {
        getAirplane(id).then(value => setChosen({...value.data}))
    }, [id])

    function deleteItem() {
        deleteAirplane(id).then(() =>
            window.location.reload()
        )
    }

    return (
        <div>
            <h3>{chosen?.id}) {chosen?.brand} - {chosen?.model}</h3>
            <h4>speed - {chosen?.speed}</h4>
            <h4>year - {chosen?.year}</h4>
            <h4>number of passengers - {chosen?.number_of_passengers}</h4>
            <h4>max range of flight - {chosen?.max_range_of_flight}</h4>
            {chosen && <Form item={chosen} do_you_wont_update_component={true}/>}
            <button onClick={deleteItem}>delete</button>
        </div>
    )
}