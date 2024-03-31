#!/bin/bash
#displays the body of the response
curl -sL -H "X-School-User-Id: $school_user_id" "$url"
