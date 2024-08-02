import yaml
from yaml import MappingNode


class CustomLoader(yaml.FullLoader):
    pass


def construct_huggingface_hub_objects(loader: CustomLoader, node: MappingNode) -> dict:
    return loader.construct_mapping(node)


CustomLoader.add_constructor('tag:yaml.org,2002:python/object:huggingface_hub.community.DiscussionWithDetails',
                             construct_huggingface_hub_objects)
CustomLoader.add_constructor('tag:yaml.org,2002:python/object:huggingface_hub.community.DiscussionComment',
                             construct_huggingface_hub_objects)
CustomLoader.add_constructor('tag:yaml.org,2002:python/object:huggingface_hub.community.DiscussionStatusChange',
                             construct_huggingface_hub_objects)
CustomLoader.add_constructor('tag:yaml.org,2002:python/object:huggingface_hub.community.DiscussionTitleChange',
                             construct_huggingface_hub_objects)
CustomLoader.add_constructor('tag:yaml.org,2002:python/object:huggingface_hub.community.DiscussionEvent',
                             construct_huggingface_hub_objects)
