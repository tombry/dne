#!/bin/bash
curl -v -X POST -u guest:guest --header "Content-Type:text/xml;charset=UTF-8" --data @API.virl http://$1:19399/simengine/rest/launch?session=APIs
