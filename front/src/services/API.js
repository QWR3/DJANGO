import axios from "axios";

const options = {
    // baseURL:'http://127.0.0.1:8000/'
    baseURL: 'http://localhost:8000/'
}

const axiosInstance = axios.create(options)

function getAirplanes() {
    return axiosInstance.get('airplane/')
}

function getAirplane(id) {
    return axiosInstance(`airplane/${id}/`)
}

function updateAirplane(item) {
    return axiosInstance({
        method: 'put',
        url: `airplane/${item.id}/`,
        data: {...item}
    })
}

function deleteAirplane(id) {
    return axiosInstance.delete(`airplane/${id}/`)
}

export {getAirplanes, getAirplane, updateAirplane, deleteAirplane}
