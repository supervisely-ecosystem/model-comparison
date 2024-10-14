import supervisely as sly
import supervisely.app.widgets as widgets
from supervisely.nn.benchmark.comparison.model_comparison import ModelComparison

import src.globals as g
import src.workflow as w


def main_func():
    models_comparison_report.hide()
    pbar.show()

    # # ==================== Workflow input ====================
    # w.workflow_input(api, project, g.session_id)
    # # =======================================================

    comp = ModelComparison(
        g.api,
        [
            # # (object detection):
            "/model-benchmark/42314_COCO 2017_001/66783_Serve YOLOv8 | v9 | v10/",
            "/model-benchmark/42314_COCO 2017_001/66783_Serve YOLOv8 | v9 | v10_001/",
            "/model-benchmark/42314_COCO 2017_001/66797_Serve YOLOv8 | v9 | v10/",
            # # (instance segmentation):
            # "/model-benchmark/42344_COCO2017 masks/66797_Serve YOLOv8 | v9 | v10/",
            # "/model-benchmark/42344_COCO2017 masks/66797_Serve YOLOv8 | v9 | v10_001/",
        ],
        output_dir=g.STORAGE_DIR + "/benchmark",
    )

    comp.visualize()
    res_dir = get_res_dir()
    comp.upload_results(g.team_id, remote_dir=res_dir)

    report = g.api.file.get_info_by_path(g.team_id, comp.get_report_link())
    g.api.task.set_output_report(g.task_id, report.id, report.name)

    models_comparison_report.set(report)
    models_comparison_report.show()
    pbar.hide()

    # ==================== Workflow output ====================
    w.workflow_output(g.api, res_dir, report)
    # =======================================================

    button.loading = False
    app.stop()


def get_res_dir():
    pass


button = widgets.Button("Compare")
button.disable()

pbar = widgets.SlyTqdm()

models_comparison_report = widgets.ReportThumbnail()
models_comparison_report.hide()

controls_card = widgets.Card(
    title="Settings",
    description="Select model evaluation reports to compare",
    content=widgets.Container(
        [
            button,
            models_comparison_report,
            pbar,
        ]
    ),
)

layout = widgets.Container(widgets=[controls_card])
app = sly.Application(layout=layout)
