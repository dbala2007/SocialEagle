from graph_query import GraphIntent


class CypherQueryBuilder:

    def build(self, query):

        if query.intent == GraphIntent.SCHEMES_FOR_BENEFICIARY:

            return (
                """
MATCH (s:SCHEME)-[:AVAILABLE_TO]->(b:BENEFICIARY)
WHERE toLower(b.name)=toLower($beneficiary)
RETURN s.name
                """,
                {
                    "beneficiary": query.beneficiary
                }
            )

        if query.intent == GraphIntent.BENEFITS_OF_SCHEME:

            return (
                """
MATCH (s:SCHEME)-[:OFFERS]->(b:BENEFIT)
WHERE toLower(s.name)=toLower($scheme)
RETURN b.name
                """,
                {
                    "scheme": query.scheme
                }
            )

        if query.intent == GraphIntent.DEPARTMENT_OF_SCHEME:

            return (
                """
MATCH (d:DEPARTMENT)-[:MANAGES]->(s:SCHEME)
WHERE toLower(s.name)=toLower($scheme)
RETURN d.name
                """,
                {
                    "scheme": query.scheme
                }
            )

        if query.intent == GraphIntent.SCHEMES_BY_DEPARTMENT:

            return (
                """
MATCH (d:DEPARTMENT)-[:MANAGES]->(s:SCHEME)
WHERE toLower(d.name)=toLower($department)
RETURN s.name
                """,
                {
                    "department": query.department
                }
            )

        raise ValueError("Unsupported query")