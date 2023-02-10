from flask import Flask, jsonify
# Instantiating my app
app = Flask(__name__)

# creating an index route for the application
@app.route('/', methods = ['GET'])
def welcoming():
    return 'Hello there, discover more of the authors of different articles.'


@app.route('/articles', methods =['GET'])
def get_authors():
    articles = {
        'article_1':{
        'Id': 1,
        'Title': 'Dis information comes to head',
        'Body': "Feb. 9, 2023 In July 2021, as Covid-19 cases began to surge again, the surgeon general warned that misinformation had led to “avoidable illnesses and death” and urged the nation’s social media giants to do more to fight the sources of it. “We’re asking them to operate with greater transparency and accountability,” the official, Dr. Vivek Murthy, said at the White House. Facebook’s vice president of global affairs, Nick Clegg, responded days later, sounding aggrieved. “It’s not great to be accused of killing people,” Mr. Clegg testily wrote in a private text message to Dr. Murthy.The platform nonetheless announced a series of new policies and took down 17 accounts linked to the “Disinformation Dozen,” a disparate group of people who shared an estimated 65 percent of all anti-vaccination content online.",
        'Author': {
            'name':'Lydia Honest',
            'age': 25,
            'contact': '+256 708059467',
            'Experience': '5 years',
            'Other articles':  23
        }
        },
        'article_2':{
        'Id': 2,
        'Title': 'FTC criticizes Apple',
        'Body': "Japan's Fair Trade Commission on Feb. 9 called for more competition to cut into virtual monopolies of U.S. technology giants Apple Inc. and Google LLC in operating systems (OS) and application market for smartphones. In a report the FTC issued that day, it pointed out that there is not enough competition in both markets. It proposed that the government introduce new legislative measures to encourage competitors to enter the markets. According to the report, Google’s Android and Apple’s iOS combined hold more than 90 percent of the market share of smartphone OS. FTC officials also found in their study that most Android users utilize Google’s app store and all users of iOS use Apple’s app store, the report said.",
        'Author': {
            'name':'Hosea Columbus',
            'age': 30,
            'contact': '+256 778643423',
            'Experience': '7 years',
            'Other articles':  30
        }
        },
        'article_3':{
        'Id': 3,
        'Title': 'Solving a machine-learning mystery',
        'Body': "Large language models like OpenAI’s GPT-3 are massive neural networks that can generate human-like text, from poetry to programming code. Trained using troves of internet data, these machine-learning models take a small bit of input text and then predict the text that is likely to come next. But that’s not all these models can do. Researchers are exploring a curious phenomenon known as in-context learning, in which a large language model learns to accomplish a task after seeing only a few examples — despite the fact that it wasn’t trained for that task. For instance, someone could feed the model several example sentences and their sentiments (positive or negative), then prompt it with a new sentence, and the model can give the correct sentiment. Typically, a machine-learning model like GPT-3 would need to be retrained with new data for this new task. During this training process, the model updates its parameters as it processes new information to learn the task. But with in-context learning, the model’s parameters aren’t updated, so it seems like the model learns a new task without learning anything at all.",
        'Author': {
            'name':'Hosea Columbus',
            'age': 28,
            'contact': '+256 7753652323',
            'Experience': '3 years',
            'Other articles':  20
        }
        }
        }
    articles_list = [{'articles':articles}]
    return jsonify(articles_list)
    