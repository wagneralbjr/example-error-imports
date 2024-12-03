from pipelines.pipeline2.etls.somezone.main2 import other_pipeline_just_to_sample



def test_other_pipeline_just_to_sample():

    some_str = "XX"

    assert other_pipeline_just_to_sample(some_str) == some_str*3