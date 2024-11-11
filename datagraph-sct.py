from json import load
from rdflib import Graph, URIRef, Namespace, Literal, RDF, OWL, RDFS
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

# Function to create a graph from a .json file.
def create_datagraph(graphUrl, json_file): 
    with open(json_file) as f:
        list_of_dict = load(f)

    # Endpoint needed to connect to the graph
    endpoint = graphUrl + "sparql"

    # Namespace of SCTPerspectivisation Ontology and
    # base url for project uris'.
    sctp = Namespace("https://github.com/mjavadf/its-conspiracy/blob/main/owl/SCTPerspectivization.owl#")
    project_url = "https://github.com/mjavadf/its-conspiracy/"

    # Creating graph, binding namespaces
    graphData = Graph()
    graphData.bind("sctp", sctp)
    graphData.bind("project", project_url)

    # Creating classes
    # Eventuality
    Eventuality = URIRef(sctp.Eventuality)
    graphData.add((Eventuality, RDF.type, OWL.Class))
    ConspiracyTheory = URIRef(sctp.ConspiracyTheory)
    graphData.add((ConspiracyTheory, RDF.type, OWL.Class))
    graphData.add((ConspiracyTheory, RDFS.subClassOf, Eventuality))

    # Lens
    Lens = URIRef(sctp.Lens)
    graphData.add((Lens, RDF.type, OWL.Class))
    Narrative = URIRef(sctp.Narrative)
    graphData.add((Narrative, RDF.type, OWL.Class))
    graphData.add((Narrative, RDFS.subClassOf, Lens))

    # Cut
    Cut = URIRef(sctp.Cut)
    graphData.add((Cut, RDF.type, OWL.Class))
    Interpretation = URIRef(sctp.Interpretation)
    graphData.add((Interpretation, RDF.type, OWL.Class))
    graphData.add((Interpretation, RDFS.subClassOf, Cut))

    # Background
    Background = URIRef(sctp.Background)
    graphData.add((Background, RDF.type, OWL.Class))
    Context = URIRef(sctp.Context)
    graphData.add((Context, RDF.type, OWL.Class))
    graphData.add((Context, RDFS.subClassOf, Background))

    # Attitude
    Attitude = URIRef(sctp.Attitude)
    graphData.add((Attitude, RDF.type, OWL.Class))
    Stance = URIRef(sctp.Stance)
    graphData.add((Stance, RDF.type, OWL.Class))
    graphData.add((Stance, RDFS.subClassOf, Attitude))

    # MediaContent
    MediaContent = URIRef(sctp.MediaContent)
    graphData.add((MediaContent, RDF.type, OWL.Class))
    Format = URIRef(sctp.Format)
    graphData.add((Format, RDF.type, OWL.Class))
    graphData.add((Format, RDFS.subClassOf, MediaContent))

    # Evidence
    Evidence = URIRef(sctp.Evidence)
    graphData.add((Evidence, RDF.type, OWL.Class))
    EvidenceType = URIRef(sctp.EvidenceType)
    graphData.add((EvidenceType, RDF.type, OWL.Class))
    graphData.add((EvidenceType, RDFS.subClassOf, Evidence))

    # Proponent
    Proponent = URIRef(sctp.Proponent)
    graphData.add((Proponent, RDF.type, OWL.Class))
    ProponentType = URIRef(sctp.ProponentType)
    graphData.add((ProponentType, RDF.type, OWL.Class))
    graphData.add((ProponentType, RDFS.subClassOf, Proponent))

    # ScientificAnalysis
    ScientificAnalysis = URIRef(sctp.ScientificAnalysis)
    graphData.add((ScientificAnalysis, RDF.type, OWL.Class))
    AnalysisType = URIRef(sctp.AnalysisType)
    graphData.add((AnalysisType, RDF.type, OWL.Class))
    graphData.add((AnalysisType, RDFS.subClassOf, ScientificAnalysis))

    # Creating relations
    hasEventuality = URIRef(sctp.hasEventuality)
    graphData.add((hasEventuality, RDF.type, OWL.ObjectProperty))
    hasLens = URIRef(sctp.hasLens)
    graphData.add((hasLens, RDF.type, OWL.ObjectProperty))
    hasCut = URIRef(sctp.hasCut)
    graphData.add((hasCut, RDF.type, OWL.ObjectProperty))
    hasBackground = URIRef(sctp.hasBackground)
    graphData.add((hasBackground, RDF.type, OWL.ObjectProperty))
    hasAttitude = URIRef(sctp.hasAttitude)
    graphData.add((hasAttitude, RDF.type, OWL.ObjectProperty))
    hasMediaContent = URIRef(sctp.hasMediaContent)
    graphData.add((hasMediaContent, RDF.type, OWL.ObjectProperty))
    hasEvidence = URIRef(sctp.hasEvidence)
    graphData.add((hasEvidence, RDF.type, OWL.ObjectProperty))
    hasProponent = URIRef(sctp.hasProponent)
    graphData.add((hasProponent, RDF.type, OWL.ObjectProperty))
    hasScientificAnalysis = URIRef(sctp.hasScientificAnalysis)
    graphData.add((hasScientificAnalysis, RDF.type, OWL.ObjectProperty))
    hasValue = URIRef(sctp.hasValue)
    graphData.add((hasValue, RDF.type, OWL.DatatypeProperty))

    n = 0
    event_uri = URIRef(project_url + "event_")
    lens_uri = URIRef(project_url + "lens_")
    cut_uri = URIRef(project_url + "cut_")
    background_uri = URIRef(project_url + "background_")
    attitude_uri = URIRef(project_url + "attitude_")
    media_uri = URIRef(project_url + "media_")
    evidence_uri = URIRef(project_url + "evidence_")
    proponent_uri = URIRef(project_url + "proponent_")
    analysis_uri = URIRef(project_url + "analysis_")
    
    # Adding triples to the graph
    for entry in list_of_dict:
        N = str(n)
        e = event_uri + N
        l = lens_uri + N
        c = cut_uri + N
        b = background_uri + N
        a = attitude_uri + N
        m = media_uri + N
        ev = evidence_uri + N
        p = proponent_uri + N
        an = analysis_uri + N
        
        # Eventuality
        graphData.add((e, RDF.type, ConspiracyTheory))
        graphData.add((e, hasValue, Literal(entry["eventuality"]["description"])))

        # Lens
        graphData.add((l, RDF.type, Narrative))
        graphData.add((l, hasValue, Literal(entry["lens"]["description"])))

        # Cut
        graphData.add((c, RDF.type, Interpretation))
        graphData.add((c, hasValue, Literal(entry["cut"]["interpretation"])))

        # Background
        graphData.add((b, RDF.type, Context))
        graphData.add((b, hasValue, Literal(entry["background"]["context"])))

        # Attitude
        graphData.add((a, RDF.type, Stance))
        graphData.add((a, hasValue, Literal(entry["attitude"]["stance"])))

        # MediaContent
        graphData.add((m, RDF.type, Format))
        graphData.add((m, hasValue, Literal(entry["mediaContent"]["format"])))

        # Evidence
        graphData.add((ev, RDF.type, EvidenceType))
        graphData.add((ev, hasValue, Literal(entry["evidence"]["description"])))

        # Proponent
        graphData.add((p, RDF.type, ProponentType))
        graphData.add((p, hasValue, Literal(entry["proponent"]["description"])))

        # ScientificAnalysis
        graphData.add((an, RDF.type, AnalysisType))
        graphData.add((an, hasValue, Literal(entry["scientificAnalysis"]["description"])))
        
        n += 1

    # Sending the graph to the database
    store = SPARQLUpdateStore()
    store.open((endpoint, endpoint))

    for triple in graphData.triples((None, None, None)):
        store.add(triple)

    store.close()

create_datagraph("http://localhost:9999/blazegraph/", "/path/to/dataset2.json")
