function getDirections() {
    const Url='https://api.mapbox.com/directions/v5/mapbox/driving/'
    const Data={
        coordinates: [40.63578,22.9510464;],
        key: 'AIzaSyDNq6BRfShX7kEGfJZQWMSvo-eYTk5PDF4'
    }

    // optional parameters
    const otherParams={
        headers:{
            "content-type":"application/json; charset=UTF-8"
        },
        mode: 'cors',
        body: Data,
        method:"GET"
    }

    fetch(Url)
    .then(data => {return data.json()})
    .then(result => {console.log(result)})
    .catch(error => {console.log(error)})

}