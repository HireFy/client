from ..version.item import Item


class Structure(Item):

    def __init__(self, json_payload):
        super().__init__(json_payload)

        self._name = json_payload.get('name', '')
        self._source_key = json_payload.get('sourceKey', '')

    @classmethod
    def from_structure(cls, structure_id, other_structure):
        return cls({
            'id': structure_id,
            'tags': other_structure.get_tags(),
            'name': other_structure.get_name(),
            'sourceKey': other_structure.get_source_key(),
        })

    def get_item_id(self):
        return self.get_id()

    def get_name(self):
        return self._name

    def get_source_key(self):
        return self._source_key

    def __eq__(self, other):
        return (
            isinstance(other, Structure)
            and self.get_name() == other.get_name()
            and self.get_source_key() == other.get_source_key()
            and self.get_item_id() == other._id
            and self.get_tags() == other._tags
        )
