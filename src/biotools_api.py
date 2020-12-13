import json
import requests

# The call to get all bio.tools entries through the api is: https://bio.tools/api/tool/?format=json.
# Unfortunately, the response is limited to n tools. To get the whole set, the next pages must be retrieve.
# use "next" in the response to get succesive entries.
 
base_call = "https://bio.tools/api/tool/?format=json"


def make_request(URL):
    try:
        response = requests.get(URL)
    except:
        print('Could not make the request')
        return
    else:
        response = json.loads(response.text)
        return(response)

def build_url(next_page, filters):
    call_template = "https://bio.tools/api/tool/?{description}{topic}{topic_id}{next_page}&format=json"
    if next_page:
        next_page = "&%s"%next_page
    else:
        next_page = ""
    desc = "description=%s"%(filters.get("description"))
    topic =  "&topic=%s"%(filters.get("topic"))
    topic_id = "&topicID=%s"%(filters.get("topic_id"))
    
    url = call_template.format(next_page=next_page, description=desc, topic=topic, topic_id=topic_id)
    return(url)


def get_all_pages(filters):
    res = []
    next_page = "page=1"
    while next_page:
        response = make_request(build_url(next_page, filters))
        print(build_url(next_page, filters))
        res = res + response["list"]
        next_page = response["next"]
        if next_page:
            next_page = next_page[1:]
            
    return(res)

def save_result(out_name, result):
    with open(out_name, 'w') as out:
        json.dump(result, out)


filters = {'topic_id':"",
            'description':"protein classification",
            'topic':"sequence analysis"}
r = get_all_pages(filters)
save_result('dual.json', r)